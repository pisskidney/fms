import os
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.conf import settings
from builder.forms import BuildHomeForm, BuildNameForm, BuildThemeForm
from builder.models import Website, Theme, Image


#@TODO this needs to be a decorator
#@REVIEW
#ADD http status code 404 etc
def is_website_id_ok(id, request, stage):
    # Website exists
    try:
        website = Website.objects.get(pk=id)
    except Website.DoesNotExist:
        return False
    # Website building left off here
    '''
    if website.build_stage != stage:
        return False
    '''
    # Website belongs to current user
    if request.user.is_authenticated():
        if request.user != website.owner:
            return False
    return True


class BuildThemeView(View):

    STAGE = 2

    def get(self, request, *args, **kwargs):
        website_id = int(kwargs['id'])
        if not is_website_id_ok(website_id, request, self.STAGE):
            #@TODO streamline errors
            return redirect('error', 1)

        build_theme_form = BuildThemeForm()
        return render(request, 'build_theme.html', {
            'build_theme_form': build_theme_form
        })

    #No checks made for post
    def post(self, request, *args, **kwargs):
        website_id = int(kwargs['id'])
        if not is_website_id_ok(website_id, request, self.STAGE):
            #@TODO streamline errors
            return redirect('error', 1)
        build_theme_form = BuildThemeForm(request.POST)
        if not build_theme_form.is_valid():
            return render(
                request, 'build_theme.html', {
                    'build_theme_form': build_theme_form
                },
                status=400
            )
        # Check if set theme and bg images exist
        try:
            theme_id = int(build_theme_form.cleaned_data['theme'])
            background_id = int(build_theme_form.cleaned_data['bg'])
            theme = Theme.objects.get(pk=theme_id)
            img = Image.objects.get(pk=background_id)
        except (Theme.DoesNotExist, Image.DoesNotExist):
            #@TODO errors
            return redirect('error', 2)

        # Update data
        website = Website.objects.get(pk=website_id)
        website.theme = theme
        website.home_background = img

        # Set stage
        website.build_stage += 1

        # Save
        website.save()
        return redirect('build_home', id=kwargs['id'])


class BuildHomeView(View):

    STAGE = 3

    def init_data(self, **kwargs):
        website_id = kwargs['id']
        website = Website.objects.get(pk=website_id)
        self.data = {
            'stage': self.STAGE,
            'bg': website.home_background.preview,
            'color1': website.theme.color1,
            'color2': website.theme.color2,
            'color3': website.theme.color3,
            'color4': website.theme.color4,
            'color5': website.theme.color5,
        }

    def get(self, request, *args, **kwargs):
        website_id = int(kwargs['id'])
        if not is_website_id_ok(website_id, request, self.STAGE):
            #@TODO errors
            return redirect('error', 1)

        self.init_data(**kwargs)

        build_home_form = BuildHomeForm()
        return render(request, 'build_home.html', {
            'build_home_form': build_home_form,
            'data': self.data,
        })

    #No checks made for post
    def post(self, request, *args, **kwargs):
        build_home_form = BuildHomeForm(request.POST)
        if not build_home_form.is_valid():
            self.init_data(**kwargs)
            return render(
                request, 'build_home.html', {
                    'build_home_form': build_home_form,
                    'data': self.data,
                },
                status=400
            )
        return redirect('payment', id=kwargs['id'])


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

        domain_type = 1
        if 'com' in request.POST:
            domain_type = 2
        elif 'own' in request.POST:
            domain_type = 3

        website = Website(
            domain_name=build_name_form.cleaned_data['name'],
            domain_type=domain_type,
            build_stage=2,
        )
        if request.user.is_authenticated():
            website.owner = request.user
        website.save()

        return redirect('build_theme', id=website.id)
