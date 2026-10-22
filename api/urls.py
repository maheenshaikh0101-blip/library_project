from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list_create, name="api_book_list"),
    path("books/<int:pk>/", views.book_detail, name="api_book_detail"),
]