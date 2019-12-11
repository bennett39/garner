from django.contrib.auth import get_user_model
from django.db import models


class ItemAccessToken(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    token = models.CharField(max_length=120)
