from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('posts.urls')),
    path('zoniha/', admin.site.urls),
]
