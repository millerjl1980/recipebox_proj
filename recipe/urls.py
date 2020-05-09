from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.index, name='home'),
    path('recipe/<int:id>', views.recipe, name='recipe'),
    path('author/<int:id>', views.author, name='author'),
    path('addauthor.html', views.add_author, name='addauthor'),
    path('addrecipe.html', views.add_recipe, name='addrecipe'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
]
