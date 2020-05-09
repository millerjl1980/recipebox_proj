from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from recipe.forms import AddRecipeForm, AddAuthorForm, LoginForm
from recipe.models import Author, Recipe
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def index(request):
    return render(request, 'index.html',
                  {'recipes': Recipe.objects.all()})


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    return render(request, 'recipe.html', {'recipe': recipe})


def author(request, id):
    author = get_object_or_404(Author, pk=id)
    # Got help from Peter on 5/7 for redering and sorting recipes
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author.html', {'author': author, 'recipes': recipes})

def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddAuthorForm()
    return render(request, 'addauthor.html', {'form': form})

def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddRecipeForm()
    return render(request, 'addrecipe.html', {'form': form})


