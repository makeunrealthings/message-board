# django_project/urls.py
from django.contrib import admin
from django.urls import path, include # new
urlpatterns = [
 path("admin/", admin.site.urls),
 path("", include("posts.urls")), # new
]
