from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('common/', include('common.urls')),
  
]


# 127.0.0.1:8000/blog