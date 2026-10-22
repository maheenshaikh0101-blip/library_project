from django.urls import path
from . import views

urlpatterns = [
    path("", views.note_list, name="note_list"),
    path("add/", views.note_create, name="note_create"),
    path("edit/<int:id>/", views.note_update, name="note_update"),
    path("remove/<int:id>/", views.note_delete, name="note_delete"),
]