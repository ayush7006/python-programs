num = int(input('enter num.-->'))
sum=0
n=num
length=len(str(num))
for i in range(length):
    r=int(n/10)
    l=n%10
    sum+=l**length
    n=r
    print(l,r,sum)
if sum==num:
    print("Armstrong")
else:
    print("not Armstrong")          


