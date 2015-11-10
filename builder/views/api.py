import json
from django.views.generic.base import View
from django.http import HttpResponse
from builder.helpers import DomainManager


class CheckDomainView(View):

    tlds = ['.com']

    def get(self, request, name, *args, **kwargs):
        domains = []
        for tld in self.tlds:
            domains.append(name + tld)
        dm = DomainManager()
        result_domain = dm.check_domains(domains)
        result_subdomain = dm.check_subdomain(name)

        result = result_domain.copy()
        result.update(result_subdomain)

        return HttpResponse(json.dumps(result))
