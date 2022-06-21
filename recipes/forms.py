from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'description',
            'recipe_image',
            'calories',
            'protein',
            'carbs',
            'fat',
            'ingredients',
            'steps',
        )
        widgets = {
            'ingredients': SummernoteWidget(),
            'steps': SummernoteWidget(),
        }
