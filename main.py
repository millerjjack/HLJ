#!/user/bin/env python
# -*- coding: utf-8 -*-

import re
import regex
from Source import ht_api
from art import *


menu = """
[1] Traceroute --> Using mtr an advanced traceroute tool trace the path of an Internet connection.
[2] Ping Test --> A common tool for testing connectivity to a host, perform a ping from our server.
[3] DNS Lookup --> Find DNS records for a domain, results are determined using the dig DNS tool.
[4] Find (A) Records --> Find forward DNS (A) records for a domain.
[5] Reverse DNS --> Find Reverse DNS records for an IP address or a range of IP addresses.
[6] Find Shared DNS Servers --> Find hosts sharing DNS servers.
[7] Zone Transfer --> Online Test of a zone transfer that will attempt to get all DNS records for a target domain.
[8] WhoIS Lookup --> Determine the registered owner of a domain or IP address block with the whois tool.
[9] GeoIP Lookup --> Find the location of an IP address using the GeoIP lookup location tool.
[10] Reverse IP Lookup --> Discover web hosts sharing an IP address with a reverse IP lookup.
[11] TCP Port Scan --> Determine the status of an Internet facing service or firewall.
[12] Subnet Lookup Online --> Determine the properties of a network subnet.
[13] HTTP Headers --> View HTTP Headers of a web site. The HTTP Headers reveal system and web application details.
[14] Page Links --> Dump all the links from a web page.
[15] AS Lookup --> Get Autonomous System Number or ASN details from an AS or an IP address.
[16] Banner Grabbing (Search) --> Discover network services by querying the service port.
"""


def addresses():
    with open('hosts.txt', 'r') as file:
        hosts = []
        for i in file.readlines():
            i = i.rstrip()
            found = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', i)
            if regex:
                hosts.extend(found)
        run(hosts)


def run(hosts):
    try:
        choice = input("Pick ya poison: ")
        if choice == '1':
            print('\n')
            print("[+] Sneaky Traceroute time >:D")
            for host in hosts:
                ht_api.lookup(1, host)

        elif choice == '2':
            print('\n')
            print("[+] A Ping Test... Really? :/")
            for host in hosts:
                ht_api.lookup(2, host)

        elif choice == '3':
            print('\n')
            print("[+] DNS Lookup...HMM-MMM ")
            for host in hosts:
                ht_api.lookup(3, host)

        elif choice == '4':
            print('\n')
            print("[+] Finding Records...")
            for host in hosts:
                ht_api.lookup(4, host)

        elif choice == '5':
            print('\n')
            print("[+] Reversing dns....")
            for host in hosts:
                ht_api.lookup(5, host)

        elif choice == '6':
            print('\n')
            print("[+] Sharing is caring <3")
            for host in hosts:
                ht_api.lookup(6, host)

        elif choice == '7':
            print('\n')
            print("[+] Attempting Zone Transfer")
            for host in hosts:
                ht_api.lookup(7, host)

        elif choice == '8':
            print('\n')
            print("[+] Who IS you???")
            for host in hosts:
                ht_api.lookup(8, host)

        elif choice == '9':
            print('\n')
            print("[+] Geo Lookup...")
            for host in hosts:
                ht_api.lookup(9, host)

        elif choice == '10':
            print('\n')
            print("[+] Reversing IP")
            for host in hosts:
                ht_api.lookup(10, host)

        elif choice == '11':
            print('\n')
            print("[+] TCP PORT SCAN RLY U COULD DO THIS MANUALLY!!!!")
            for host in hosts:
                ht_api.lookup(11, host)

        elif choice == '12':
            print('\n')
            print("[+] Subnet Lookup....")
            for host in hosts:
                ht_api.lookup(12, host)

        elif choice == '13':
            print('\n')
            print("[+] Gathering HTTP Headers.....")
            for host in hosts:
                ht_api.lookup(13, host)

        elif choice == '14':
            print('\n')
            print("[+] Page links coming up....")
            for host in hosts:
                ht_api.lookup(14, host)

        elif choice == '15':
            print('\n')
            print("[+] AS Lookup I guess...")
            for host in hosts:
                ht_api.lookup(15, host)

        elif choice == '16':
            print('\n')
            print("[+] ohh juicy banners")
            for host in hosts:
                ht_api.lookup(16, host)

    except KeyboardInterrupt:
        print('\nTerminated')
        quit()
    except ValueError:
        pass


Art = text2art(" HLJ", "rnd-large")
print(Art)

print(menu)
addresses()
