from django.urls import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('rules/', views.rules, name='rules'),
    path('about/', views.about, name='about'),
]