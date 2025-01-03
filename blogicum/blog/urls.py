from django.urls import path
from blog import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/<str:category>', views.index, name='index_filtred'),
    path('category_posts/', views.category_posts, name='category_posts'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
]