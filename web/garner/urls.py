from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('connect/', include('connect.urls')),
    path('sheets/', include('sheets.urls')),
]
