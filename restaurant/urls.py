from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu_view, name='menu'),
    path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
]