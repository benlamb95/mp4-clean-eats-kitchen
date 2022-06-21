from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
# https://www.youtube.com/watch?v=hpo18rVZhG4&list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL&index=51


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'likes')
    list_display = ('title', 'created_on', 'status',)
    search_fields = ('title', 'description', 'ingredients', 'steps')
    summernote_fields = ('description', 'ingredients', 'steps')
    actions = ['approve_recipe']

    def approve_recipe(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'recipe', 'added_on', 'approved')
    list_filter = ('approved', 'added_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
