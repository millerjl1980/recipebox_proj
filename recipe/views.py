from django.shortcuts import render, get_object_or_404

from recipe.models import Author, Recipe

# Create your views here.


def index(request):
    return render(request, 'index.html',
                  {'recipes': Recipe.objects.all(),
                   'authors': Author.objects.all()})


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    return render(request, 'recipe.html', {'recipe': recipe})


def author(request, id):
    author = get_object_or_404(Author, pk=id)
    return render(request, 'author.html', {'author': author})
