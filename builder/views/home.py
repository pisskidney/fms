from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        sites = {}
        for site in user.websites.all():
            # Subdomain
            if site.domain_type is 1:
                part1 = site.domain_name
                part2 = settings.SITE_NAME
            # Custom domain; Already own domain
            else:
                part1 = 'www'
                part2 = site.domain_name
            part3 = 'com'
            sites[site.id] = {
                'name': site.domain_name,
                'url': '.'.join([part1, part2, part3]),
            }
        return render(request, 'home/home.html', {
            'sites': sites,
        })
