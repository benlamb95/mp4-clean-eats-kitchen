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
    path('recipes/create', views.CreateRecipe.as_view(), name='create_recipe'),
    path('recipes/update/<slug:slug>', views.UpdateRecipe.as_view(), name='update_recipe'),
    path('recipes/delete/<slug:slug>', views.DeleteRecipe.as_view(), name='delete_recipe'),
    path('recipes/my_profile', views.UserProfileView.as_view(), name='profile'),
    path('search_recipe', views.SearchRecipe.as_view(), name='search_recipe'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_likes'),
]
