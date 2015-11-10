import requests
import xml.etree.ElementTree as ET
from django.conf import settings
from builder.models import Website


nc = settings.DOMAIN_APIS['namecheap']


class Namecheap(object):
    params = {
        'ApiUser': nc['APIUSER'],
        'ApiKey': nc['APIKEY'],
        'UserName': nc['USERNAME'],
        'ClientIp': nc['CLIENTIP'],
        'Command': 'namecheap.domains.check',
        'DomainList': None
    }

    ns = {'default': 'http://api.namecheap.com/xml.response'}
    URL = nc['URL']
    response_tag = 'CommandResponse'

    def __init__(self):
        self.errors = False

    def build_url(self, domains):
        url_params = ''
        for k, v in self.params.iteritems():
            url_params += '&'
            url_params += k
            url_params += '='
            if k == 'DomainList':
                url_params += ','.join(domains)
            else:
                url_params += v
        url_params = url_params[1:]
        full_url = self.URL + url_params
        return full_url

    def check_domains(self, domains):
        '''
        This function checks tld domains' availability
        domains = ['foo.com', 'bar.net'] etc
        @return = {'.com': True, '.net': False} etc
        '''
        url = self.build_url(domains)
        response = requests.get(url)
        root = ET.fromstring(response.content)
        resp = root.find('default:' + self.response_tag, self.ns)
        result = {}
        for child in resp:
            is_available_str = child.get('Available')
            is_available = True if is_available_str == 'true' else False
            result[child.get('Domain')] = is_available
        return result


class DomainManager(object):

    domain_class = Namecheap

    def __init__(self):
        self.errors = False

    def check_domains(self, domains):
        dc = self.domain_class()
        return dc.check_domains(domains)

    def check_subdomain(self, subdomain):
        result = {}
        websites = Website.objects.filter(domain_name__exact=subdomain)
        website = websites.filter(
            domain_type__exact=Website.CHOICES_DOMAIN_TYPE[0][0])
        result['subdomain'] = True if not website else False
        return result
