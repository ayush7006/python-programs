num1 = int(input("enter low num-->"))
num2 = int(input("enter upr num-->"))

for i in range(num1,num2 + 1):
    if i>1:
        for a in range(2, i):
            if i%a==0:
                break
        else :
            print(i)  
