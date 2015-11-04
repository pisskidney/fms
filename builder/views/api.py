import requests
import json
import xml.etree.ElementTree as ET
from django.views.generic.base import View
from django.http import HttpResponse


class CheckDomainView(View):

    API_USER = 'petisnnake'
    API_KEY = '54d95e465c62458ba07b1d2d9656a09a'
    USERNAME = 'petisnnake'
    URL = 'https://api.sandbox.namecheap.com/xml.response?'
    CLIENT_IP = '109.102.16.125'
    COMMAND = 'namecheap.domains.check'

    def get(self, request, domain, *args, **kwargs):
        url = self.URL + 'ApiUser=%s&ApiKey=%s&UserName=%s&ClientIp=%s&Command=%s&DomainList=%s' % (
                self.API_USER,
                self.API_KEY,
                self.USERNAME,
                self.CLIENT_IP,
                self.COMMAND,
                domain + '.com',
            )
        r = requests.get(url)
        root = ET.fromstring(r.content)

        print root.attrib['Status']
        if root.attrib['Status'] != 'OK':
            raise Exception('There was an unexpected error')
        com = root[3][0].attrib['Available']
        if com == 'true':
            com = True
        else:
            com = False
        inhouse = True

        result = {
            'inhouse': inhouse,
            'com': com
        }

        return HttpResponse(json.dumps(result))
