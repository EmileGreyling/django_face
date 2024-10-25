<p align="center">
  <img src="https://capsule-render.vercel.app/api?text=Django%20Face&animation=fadeIn&type=soft&color=gradient&height=150"/>
</p>

### 📄 Overview
This project is a face recognition web application built using Django and JavaScript with jQuery. The app allows users to upload images of faces and create a database of faces connected to their account. The app can then identify the faces in the uploaded images that are present in the database.

Link to YouTube video showing how the project works: https://youtu.be/mLy7rvJNfYU

### 🔍 Distinctiveness and Complexity
This project stands out for several reasons. First, it integrates face recognition technology into a web application that leverages Django's powerful backend framework and JavaScript for frontend interactions. The combination of these technologies creates a dynamic, full-stack project that is far more complex than the simpler CRUD-based projects often seen in web development.

I chose to use the `face_recognition` library due to its ease of use and simplicity in implementing face detection and recognition functionalities. However, this simplicity didn’t come without challenges. I initially encountered difficulties installing the library, facing numerous build errors. After troubleshooting, I discovered that the issue was related to dependencies missing on my system—specifically, the `cmake` tool needed to be installed. Overcoming these challenges was a significant part of the project's complexity.

In addition to installation issues, I struggled with drawing bounding boxes and annotating names around detected faces in the images. The library provided the core functionality, but customizing the detection to display results in a user-friendly way required additional effort.

I decided to use **jQuery** for the frontend because I wanted a simple solution for making asynchronous requests without reloading the page and without writing a lot of tedious Javascript code. Given that the majority of the project’s complexity lay in the backend, I chose not to add unnecessary complexity to the frontend. jQuery enabled me to handle form submissions and image uploads seamlessly, using AJAX to send data to the Django backend without page refreshes.

This project's distinctiveness also lies in its ability to handle real-world, user-generated data in the form of uploaded images. Implementing face recognition efficiently—processing potentially large image files, encoding faces, and comparing them against a database—presents significant technical challenges. Additionally, the app’s mobile-responsive design ensures that users can interact with the system across various devices, adding to its overall complexity.

### 📂 File Structure

- ```admin.py:``` Contains configuration for the admin page of the application.

- ```models.py:``` Defines the Face and User models used - in the app.

- ```views.py:``` Handles HTTP requests and responses, including image upload and face recognition.

- ```urls.py:``` Contains a list of URL paths for the app.

- ```templates:``` Contains HTML templates for the app's UI.

- ```static/djangoface/app.js:``` Holds the JavaScript code to open modals and send HTTP requests without having to refresh the page.

- ```static/djangoface/styles.css:``` Holds the CSS styles for the app.

- ```requirements.txt:``` Lists dependencies required to run the app.

### 💻 How to Run the Application
1. Clone the repository and navigate to the project directory.
2. Install dependencies using the following command:

    ```pip install -r requirements.txt```.

3. Run the app using this command: 

    ```python manage.py runserver```.

4. Access the app at http://localhost:8000.

### ⚙️ Technical Details
The app uses the `face_recognition` library for face recognition, which is a Python wrapper around the `dlib` library. This library provides a straightforward interface for face detection, encoding, and comparison, enabling efficient and accurate face recognition. 

However, working with the library presented its own challenges. Installing `face_recognition` required me to install additional dependencies, including `cmake`, to resolve build errors that were initially preventing the library from functioning properly. Once installation was complete, implementing custom features, such as drawing bounding boxes around recognized faces and labeling them with names, involved significant trial and error, adding to the complexity.

### 🔒 User Authentication
The app uses Django's built-in authentication system to manage user accounts. Users can register, log in, and log out of the app, with each user having their own database of faces. Django’s permission system was also utilized to ensure that only authenticated users could access certain views and functionalities, such as uploading images or adding faces to the database. This ensures both security and privacy, as users’ face data is protected by the app’s authentication and authorization mechanisms.

### 👀 Face Recognition Process

The app's face recognition functionality works as follows:

- **Image Upload:** Users upload an image containing one or more faces.
- **Face Detection:** The app uses `OpenCV` (through the `face_recognition` library) to detect faces in the uploaded image.
- **Face Encoding:** Detected faces are encoded into a numerical format, which can be compared against known faces in the database.
- **Database Search:** The app searches for matching face encodings in the user's database of faces.
- **Identification:** If a match is found, the app draws a bounding box around each recognized face and labels it with the person’s name. If no match is found, the face is labeled as "Unknown."

### 📱 Mobile-Responsive Design
The app's user interface (UI) was built using HTML, CSS, and JavaScript, with Bootstrap ensuring a mobile-responsive layout. This allows the app to be accessible on a wide variety of devices, from desktop computers to smartphones, providing a consistent user experience. The mobile responsiveness was crucial, as the app's target users might access it on different screen sizes.

### 🎉 Conclusion
This project demonstrates the ability to build a robust, full-stack web application integrating cutting-edge face recognition technology with Django's backend capabilities. The distinctiveness lies in the combination of technologies and the challenges faced in implementing a secure, scalable, and responsive system. The complexity of handling real-world image data, combined with ensuring a seamless user experience, makes this project a unique contribution to the final assignment in CS50’s Web Programming course.


### 📃 Acknowledgments
This project includes some adapted code from a [tutorial by Traversy Media](https://www.youtube.com/watch?v=QSTnwsZj2yc) on how to recognize faces in a image with python.
