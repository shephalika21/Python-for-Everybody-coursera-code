# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
names = list()

url = input('Enter the url - ')
count = int(input('Enter count:'))
pos = int(input('Enter position:'))

while count>0:
    print("Retrieving:", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    name = tags[pos-1].string
    print(name)
    names.append(name)
    url = tags[pos-1]['href']
    count = count - 1

print(names[-1])
