from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('category_posts/<str:category>', views.category_posts, name='category_posts'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
]