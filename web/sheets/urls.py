from django.urls import path, include

from .views import UpdateView

app_name = 'sheets'
urlpatterns = [
    path('', UpdateView.as_view(), name='Update')
]
