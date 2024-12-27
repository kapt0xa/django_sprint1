from django.urls import path
from blog import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('category_posts/', views.category_posts, name='category_posts'),
    path('post_detail/', views.post_detail, name='post_detail'),
]