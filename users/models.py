from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_img", default="images/None/default.jpg", blank=True) 

    def __str__(self):
        return f'{self.user.username} Profile'