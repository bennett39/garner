from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from garner import environment as env
from lib.client import client
from .models import ItemAccessToken


class ConnectView(LoginRequiredMixin, View):
    def get(self, request):
        context = dict(plaid_environment=env.PLAID_ENVIRONMENT, plaid_public_key=env.PLAID_PUBLIC_KEY)
        return render(request, 'connect/connect.html', context)

    def post(self, request):
        public_token = request.POST.get('public_token')
        access_token = self.get_access_token(public_token)

        item_access_token = ItemAccessToken(
            user=request.user,
            token=access_token
        )
        item_access_token.save()

        return redirect('connect:connect')

    @staticmethod
    def get_access_token(public_token):
        exchange_response = client.Item.public_token.exchange(public_token)
        access_token = exchange_response['access_token']
        return access_token

