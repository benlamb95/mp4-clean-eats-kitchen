from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Added"))


class Recipe(models.Model):
    """Recipe Model"""
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              null=False,
                              blank=False,
                              related_name='owner')
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.CharField(max_length=300)
    recipe_image = CloudinaryField('image', default='placeholder')
    calories = models.CharField(max_length=40, blank=False,
                                null=False, default=0)
    protein = models.CharField(max_length=40, blank=False,
                               null=False, default=0)
    carbs = models.CharField(max_length=40, blank=False, null=False, default=0)
    fat = models.CharField(max_length=40, blank=False, null=False, default=0)
    ingredients = models.TextField(blank=False,
                                   null=False, default='Enter Ingredients')
    steps = models.TextField(blank=False,
                             null=False, default='Enter Steps')
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name="recipe_likes",
        blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)

    def number_of_likes(self):
        return self.likes.count()

    # https://stackoverflow.com/questions/837828/how-do-i-create-a-slug-in-django
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)


class Comment(models.Model):
    """Comments Model"""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    name = models.CharField(max_length=80)
    body = models.TextField()
    added_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User,
        related_name="comment_likes",
        blank=True
    )
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['added_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def number_of_likes(self):
        return self.likes.count()
