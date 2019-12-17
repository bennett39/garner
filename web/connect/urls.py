from django.urls import path, include

from .views import ConnectorView

app_name = 'connect'
urlpatterns = [
    path('', ConnectorView.as_view(), name='connect')
]
