from django.urls import path, include

from .views import ConnectView

app_name = 'connect'
urlpatterns = [
    path('', ConnectView.as_view(), name='connect')
]
