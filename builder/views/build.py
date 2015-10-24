from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from builder.forms import BuildHomeForm, BuildNameForm


class BuildHomeView(View):
    def get(self, request, *args, **kwargs):
        build_home_form = BuildHomeForm()
        return render(request, 'build_home.html', {
            'build_home_form': build_home_form
        })

    def post(self, request, *args, **kwargs):
        build_home_form = BuildHomeForm(request.POST)
        if not build_home_form.is_valid():
            return render(
                request, 'build_home.html', {
                    'build_home_form': build_home_form
                },
                status=400
            )
        return redirect('account')


class BuildNameView(View):
    def get(self, request, *args, **kwargs):
        build_name_form = BuildNameForm()
        return render(request, 'build_name.html', {
            'build_name_form': build_name_form
        })

    def post(self, request, *args, **kwargs):
        build_name_form = BuildNameForm(request.POST)
        if not build_name_form.is_valid():
            return render(
                request, 'build_name.html', {
                    'build_name_form': build_name_form
                },
                status=400
            )
        return redirect('account')
