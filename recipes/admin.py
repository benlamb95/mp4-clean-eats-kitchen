from django.contrib import admin
from .models import Recipe, RecipeIngredient, Step, Comment

# Register your models here.
# https://www.youtube.com/watch?v=hpo18rVZhG4&list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL&index=51


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0


class RecipeStep(admin.StackedInline):
    model = Step
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fieldsets = []
    inlines = [RecipeIngredientInline, RecipeStep]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'recipe', 'added_on', 'approved')
    list_filter = ('approved', 'added_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(RecipeIngredient)
admin.site.register(Step)
