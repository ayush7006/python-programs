from turtle import clear


d = {'january':'2200','fabruary':'2350','march':'2600','april':'2130','may':'2190'}
a = int(d['january'])
b = int(d['fabruary'])
c = int(d['march'])
print("1. In Feb, how many dollars you spent extra compare to January",+ b-a)
print('2. total expense in first quarter',+ a+b+c)
ex = 2000
if ex in d.values():
    print('3. you spent exactly 2000 dollar')
else :
    print('3. you spent not exactly 2000 dollar')
d['april'] = 1930
print('4. April and got a refund of 200 now total is',+ d['april'])
d['june'] = 1980
print('5. june added',+ d['june'])