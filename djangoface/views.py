from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import reverse, render

from PIL import Image, ImageDraw, ImageFont
import face_recognition
import base64
import json
from io import BytesIO

from .models import Face, User


@login_required
def index(request):
    if request.method == "POST":
        known_faces = Face.objects.filter(user=request.user)
        known_face_encodings = []
        known_face_names = []

        for face in known_faces:
            image_of_known_person = face_recognition.load_image_file(
                f"media/{face.face}"
            )
            known_person_encoding = face_recognition.face_encodings(
                image_of_known_person
            )[0]

            known_face_encodings.append(known_person_encoding)
            known_face_names.append(face.name)

        image = face_recognition.load_image_file(request.FILES["image"])

        # Find faces in test image
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        # Convert to PIL format
        pil_image = Image.fromarray(image)

        # Create a ImageDraw instance
        draw = ImageDraw.Draw(pil_image)

        # Loop through faces in image
        for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings
        ):
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding
            )

            name = "Unknown Person"

            # If match
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # Draw box around face
            draw.rectangle(((left, top), (right, bottom)), outline=(13, 110, 253))

            # Draw label
            font = ImageFont.load_default()
            ascent, descent = font.getmetrics()
            text_width = font.getmask(name).getbbox()[2]
            text_height = font.getmask(name).getbbox()[3] + descent

            draw.rectangle(
                ((left, bottom - text_height - 10), (right, bottom)),
                fill=(13, 110, 253),
                outline=(13, 110, 253),
            )
            draw.text(
                (left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255)
            )
        del draw

        # Convert PIL image to bytes
        buffered = BytesIO()
        pil_image.save(buffered, format="JPEG")
        img_bytes = buffered.getvalue()

        # Encode image bytes to base64
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')

        # Return image as base64 encoded string
        return HttpResponse(json.dumps({'image': img_base64}), content_type="application/json")

    return render(request, "djangoface/index.html")


@login_required
def faces(request):
    query = request.GET.get('q')

    if request.method == "POST":
        name = request.POST["name"]
        image = request.FILES["image"]

        Face.objects.create(user=request.user, name=name, face=image)

        # Create new face
        print(name)

    if query:
        faces = Face.objects.filter(user=request.user, name__icontains=query).order_by("name")
    else:
        faces = Face.objects.filter(user=request.user).order_by("name")

    return render(request, "djangoface/faces.html", {"faces": faces})


@login_required
def delete_face(request, id):
    face = Face.objects.filter(pk=id).first()

    if request.user == face.user:
        face.delete()

    return HttpResponseRedirect(reverse("faces"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "djangoface/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "djangoface/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request,
                "djangoface/register.html",
                {"message": "Passwords must match."},
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "djangoface/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "djangoface/register.html")
