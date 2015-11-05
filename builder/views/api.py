import json
from django.views.generic.base import View
from django.http import HttpResponse
from builder.helpers import get_domain_manager


class CheckDomainView(View):

    tlds = ['.com']

    def get(self, request, domain, *args, **kwargs):
        domains = []
        for tld in self.tlds:
            domains.append(domain + tld)
        DomainManager = get_domain_manager()
        dm = DomainManager(domains)
        dm.check_domains()
        result = {}
        print domains
        print dm.errors
        if not dm.errors:
            for tld in self.tlds:
                result[tld] = False
                if dm.is_valid(domain + tld):
                    result[tld] = True
        else:
            for tld in self.tlds:
                result[tld] = None

        return HttpResponse(json.dumps(result))
