#!/user/bin/env python
# -*- coding: utf-8 -*-

import requests

API_KEY = "c6b9d78d9a2e3cccb0668d2899a2651c91c7acc4fc8cd2a3b71542d9a1bfa6897c58ed553bae4e96"


def ht_api(choice, host):
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
    request_url = request_urls[choice-1]
    response = requests.get(request_url, params=params)
    print(response.text, file=open("juicy.txt", "a"))
    print("i spat the results into a txt file called juicy...")
