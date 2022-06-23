#!/user/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from datetime import datetime
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
import time

li = "\n____________________________________________________________________________________________________________\n"
API_KEY = ""


class Loader:
    def __init__(self, desc="[+] Working....", end="[+] Done!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            time.sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


def runner():
    if __name__ == "__main__":
        with Loader("[+] Working..."):
            for i in range(10):
                time.sleep(0.25)
    loader = Loader("[+] Working...").start()

    for i in range(10):
        time.sleep(0.25)
    loader.stop()


def lookup(choice, host):
    runner()
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
        pretty = json.loads(response.text)
        data = json.dumps(pretty, indent=4)
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
