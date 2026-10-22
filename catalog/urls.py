from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.book_list, name="book_list"),
    path("about/", views.about, name="about"),
    path("add/", views.book_create, name="book_create"),
    path("edit/<int:id>/", views.book_update, name="book_update"),
    path("remove/<int:id>/", views.book_delete, name="book_delete"),
]
