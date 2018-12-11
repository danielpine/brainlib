import json as j
import os
import random
import re
import sys
import threading
import time

from requests_html import HTMLSession

# print (sys.path)


def check_domain(domain):
    session = HTMLSession()
    data = {'domain': domain, 'search': ''}
    r = session.post(
        'https://www.dynadot.com/zh/domain/io.html', data=data, verify=True)
    print()
    print(
        r.html.find('.table-responsive', first=True).text.replace('\n', '\t'))
    print()


while True:
    domain = input("Type q to quit,\nType a domain:\n> ")
    if domain == 'q':
        break
    else:
        check_domain(domain)
