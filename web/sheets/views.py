from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from connect.models import ItemAccessToken
from lib.fetch import fetch_transactions
from lib.transform import transform_to_sheets


class UpdateView(LoginRequiredMixin, View):
    def get(self, request):
        token = ItemAccessToken.objects.first()
        options = dict(start_date='2019-11-01', end_date='2019-11-30')
        transactions = fetch_transactions(token.token, **options)
        updates = transform_to_sheets(transactions)
        context = dict(transactions=updates)
        return render(request, 'sheets/update.html', context)

    def post(self, request):
        return redirect('sheets:update')
