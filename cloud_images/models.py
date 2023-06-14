from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.

class CloudImage(models.Model):

    image = CloudinaryField('image')