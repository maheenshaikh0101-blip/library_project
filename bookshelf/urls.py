from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("accounts/", include("accounts.urls")),
    path("notes/", include("notes.urls")),
    path("", include("catalog.urls")),
]