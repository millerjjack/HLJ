#!/user/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from datetime import datetime

li = "\n______________________________________________________\n"
API_KEY = ""


def lookup(choice, host):
    request_urls = [
        "https://api.hackertarget.com/mtr/",
        "https://api.hackertarget.com/nping/",
        "https://api.hackertarget.com/dnslookup/",
        "https://api.hackertarget.com/hostsearch/",
        "https://api.hackertarget.com/reversedns/",
        "https://api.hackertarget.com/findshareddns/",
        "https://api.hackertarget.com/zonetransfer/",
        "https://api.hackertarget.com/whois/",
        "https://api.hackertarget.com/geoip/",
        "https://api.hackertarget.com/reverseiplookup/",
        "https://api.hackertarget.com/nmap/",
        "https://api.hackertarget.com/subnetcalc/",
        "https://api.hackertarget.com/httpheaders/",
        "https://api.hackertarget.com/pagelinks/",
        "https://api.hackertarget.com/aslookup/",
        "https://api.hackertarget.com/bannerlookup/"
    ]
    params = {'q': host,
              'apikey': API_KEY}
    if choice == 16:
        request_url = request_urls[choice - 1]
        response = requests.get(request_url, params=params)
        load = json.loads(response.text)
        data = json.dumps(load, indent=4)
        now = datetime.now()
        now = now.strftime("\ndate: %Y/%m/%d, Time: H%H M%M")
        final = request_url[29:] + now + " target: " + host + li + data + li
        print(final, file=open("juicy.txt", "a"))
    else:
        request_url = request_urls[choice - 1]
        response = requests.get(request_url, params=params)
        now = datetime.now()
        now = now.strftime("\ndate: %Y/%m/%d, Time: H%H M%M")
        final = request_url[29:] + now + " target: " + host + li + response.text + li
        print(final, file=open("juicy.txt", "a"))
