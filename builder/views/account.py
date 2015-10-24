from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import View


class AccountView(View):
    def get(self, request):
        return render(request, 'account.html')
