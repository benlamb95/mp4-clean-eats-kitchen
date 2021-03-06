from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Recipe
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')[0:3]
    template_name = 'index.html'


class AllRecipes(generic.ListView):
    """View to show a list of all recipes"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('title')
    template_name = 'all_recipes.html'
    paginate_by = 6


class RecipeDetails(View):
    """View to see indivdual recipe"""
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('added_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_view.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('added_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_view.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class CreateRecipe(View):
    """Creating a Recipe"""

    def get(self, request):
        context = {'form': RecipeForm()}
        return render(request, 'create_recipe.html', context)

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = self.request.user
            form.save()
            messages.success(request, "The recipe is awaiting approval...")
            return redirect('all_recipes')
        else:
            messages.error(request,
                           'Error: Form is not valid. Please re-check')
            context = {'form': form}
            return render(request, 'create_recipe.html', context)


class UpdateRecipe(UpdateView):
    """Updating a Recipe"""
    model = Recipe
    template_name = 'update_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('profile')


class DeleteRecipe(DeleteView):
    """Deleting a Recipe"""
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('profile')


# https://www.youtube.com/watch?v=AGtae4L5BbI&t=87s
# https://learndjango.com/tutorials/django-search-tutorial
def SearchRecipe(request):
    """function to search recipes by title, description and ingredients"""
    if request.method == "GET":
        searched = request.GET['searched']
        recipes = Recipe.objects.filter(
            Q(title__icontains=searched) |
            Q(ingredients__icontains=searched)
        )
        return render(request, 'search_recipe.html',
                      {'searched': searched, 'recipes': recipes})
    else:
        return render(request, 'search_recipe.html', {})


class UserProfileView(LoginRequiredMixin, ListView):
    """View a created recipe"""
    template_name = "profile.html"
    model = Recipe
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        return Recipe.objects.filter(owner=user)


class RecipeLike(View):
    """Liking a Recipe"""
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_view', args=[slug]))
