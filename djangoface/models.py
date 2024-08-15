from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Face(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploader")
    name = models.CharField(max_length=747)
    face = models.ImageField(upload_to="faces")

    def delete(self, *args, **kwargs):
        self.face.delete()
        super(Face, self).delete(*args, **kwargs)

    def __str__(self):
        return f"Face #{self.id}: {self.name}"
