import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter url: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None
    print('Error !!!!')
count = 0
sum = 0
for item in js["comments"]:
    x = int(item['count'])
    sum += x
    count += 1
print("Count:", count)
print("Sum:", sum)
