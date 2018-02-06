import re
hand = open('regex_sum_73463_data.txt')
sum = 0
x = hand.read()
stuff = re.findall('[0-9]+',x)
for i in stuff:
    num = int(i)
    sum = sum+num
print(sum)
"""
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    print(stuff)
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
"""
