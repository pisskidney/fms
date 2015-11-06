import os
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.conf import settings
from builder.forms import BuildHomeForm, BuildNameForm
from builder.models import Website


#@TODO this needs to be a decorator
#@REVIEW
#ADD http status code 404 etc
def is_website_id_ok(id, request):
    # Website exists
    try:
        website = Website.objects.get(pk=id)
    except Website.DoesNotExist:
        return False
    # Website building left off here
    if website.build_stage != 2:
        return False
    # Website belongs to current user
    if request.user.is_authenticated():
        if request.user != website.owner:
            return False
    return True


class BuildHomeView(View):
    def get(self, request, *args, **kwargs):
        website_id = int(kwargs['id'])
        if not is_website_id_ok(website_id, request):
            return redirect('error', 1)

        build_home_form = BuildHomeForm()
        return render(request, 'build_home.html', {
            'build_home_form': build_home_form
        })

    #No checks made for post
    def post(self, request, *args, **kwargs):
        build_home_form = BuildHomeForm(request.POST, request.FILES)
        if not build_home_form.is_valid():
            return render(
                request, 'build_home.html', {
                    'build_home_form': build_home_form
                },
                status=400
            )
        filename = kwargs['id'] + '_home_bg.jpg'
        path = os.path.join(settings.UPLOADS_DIR, filename)
        with open(path, 'wb+') as dest:
            for chunk in request.FILES['background']:
                dest.write(chunk)
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

        return redirect('build_home', id=website.id)
