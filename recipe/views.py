from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from recipe.forms import AddRecipeForm, AddAuthorForm, LoginForm
from recipe.models import Author, Recipe
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

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
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

# https://pythonprogramming.net/user-login-logout-django-tutorial/
def logoutview(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )

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

# https://www.youtube.com/watch?time_continue=399&v=Tja4I_rgspI&feature=emb_logo
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
@login_required
def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.author.name = form.cleaned_data.get('name')
            user.author.bio = form.cleaned_data.get('bio')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = AddAuthorForm()
    return render(request, 'addauthor.html', {'form': form})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddRecipeForm()
    return render(request, 'addrecipe.html', {'form': form})


