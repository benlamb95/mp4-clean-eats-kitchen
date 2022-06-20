from . import views
from django.urls import path


urlpatterns = [
    path(
        '',
        views.RecipeList.as_view(),
        name='home'
    ),
    path('recipes/all_recipes', views.AllRecipes.as_view(), name='all_recipes'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_view'),
]
