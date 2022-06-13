from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Added"))


class Recipe(models.Model):
    owner = models.ForeignKey(User,  
                              on_delete=models.CASCADE,
                              null=False,
                              blank=False,
                              related_name='owner')
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    recipe_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name="recipe_likes",
        blank=True
    )
