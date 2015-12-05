import os
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.conf import settings
from builder.forms import BuildHomeForm, BuildNameForm
from builder.models import Website


class PaymentView(View):
    def get(self, request, *args, **kwargs):
        # If website owner is not set, set it
        website = Website.objects.get(pk=kwargs['id'])
        website.owner = request.user
        website.save()
        
        #@TODO For now just redirect
        return redirect('home')

    def post(self, request, *args, **kwargs):
        return redirect('payment')
