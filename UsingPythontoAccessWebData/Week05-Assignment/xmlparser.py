import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter the url - ')
print('Retrieving', url)
xmlfile = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(xmlfile), 'characters')
sum = 0
count = 0
stuff = ET.fromstring(xmlfile)
counts = stuff.findall('.//count')
#print('Count:', len(counts))
#print(counts)

for item in counts:
    sum += int(item.text)
    count += 1

print('Count:', count)
print('Sum:', sum)
