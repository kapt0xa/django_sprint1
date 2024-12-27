from django.urls import path
from pages import views

urlpatterns = [
    path('rules/', views.rules, name='index'),
    path('about/', views.about, name='about'),
]