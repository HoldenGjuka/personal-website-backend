from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('github_logo/', views.github_logo, name='github_logo')
]