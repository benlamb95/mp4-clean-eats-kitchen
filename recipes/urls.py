from . import views
from django.urls import path, include


urlpatterns = [
    path(
        '',
        views.RecipeList.as_view(),
        name='home'
    ),
    path('summernote/', include('django_summernote.urls')),
    path('recipes/all_recipes', views.AllRecipes.as_view(), name='all_recipes'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_view'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_likes'),
]
