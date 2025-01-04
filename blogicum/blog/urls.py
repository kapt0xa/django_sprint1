from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<str:category>/", views.category_posts, name="category_posts"),  # noqa: E501,F401
    path("posts/<int:id>/", views.post_detail, name="post_detail"),
]
