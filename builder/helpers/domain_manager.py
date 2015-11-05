import requests
import xml.etree.ElementTree as ET


def get_domain_manager():
    return Namecheap


#@TODO get from settings / change to prod settings
class Namecheap(object):
    params = {
        'ApiUser': 'petisnnake',
        'ApiKey': '54d95e465c62458ba07b1d2d9656a09a',
        'UserName': 'petisnnake',
        'ClientIp': '109.102.16.125',
        'Command': 'namecheap.domains.check',
        'DomainList': None
    }

    ns = {'default': 'http://api.namecheap.com/xml.response'}
    URL = 'https://api.sandbox.namecheap.com/xml.response?'
    response_tag = 'CommandResponse'

    def __init__(self, domains):
        self.domains = domains
        self.errors = False
        self.url = self.build_url()

    def build_url(self):
        url_params = ''
        for k, v in self.params.iteritems():
            url_params += '&'
            url_params += k
            url_params += '='
            if v is None:
                url_params += ','.join(self.domains)
            else:
                url_params += v
        url_params = url_params[1:]
        full_url = self.URL + url_params
        return full_url

    def check_domains(self):
        url = self.url
        response = requests.get(url)
        root = ET.fromstring(response.content)
        resp = root.find('default:' + self.response_tag, self.ns)
        self.checks = {}
        if resp is None:
            self.errors = True
            return
        for child in resp:
            if child.get('Domain') not in self.domains:
                #@TODO streamline errors
                self.errors.append('Something went wrong. #0002')
                break
            is_available_str = child.get('Available')
            is_available = True if is_available_str == 'true' else False
            self.checks[child.get('Domain')] = is_available

    def is_valid(self, url):
        '''Always use check_domains() first.'''
        return self.checks[url]
