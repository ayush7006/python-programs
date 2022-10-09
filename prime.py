num = int(input("enter num-->"))

if  num == 1:
    print("not prime num")
if num > 1 :
    for i in range(2,num) :
        if num % i == 0:
            print("not prime num") 
            break  
        else:
            print('its a prime number')
            break