from django.urls import path, include

from .views import ConnectorView

app_name = 'transactions'
urlpatterns = [
    path('connect/', ConnectorView.as_view(), name='connect')
]
