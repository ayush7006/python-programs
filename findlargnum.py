num1 = int(input("enter num 1 -->"))
num2 = int(input("enter num 2 -->"))
num3 = int(input("enter num 3 -->"))

if num1>num2 and num1>num3:
    print(num1,"is largerst")
elif num2>num1 and num2>num3:
    print(num2,"is largerst")
elif num3>num2 and num1<num3:
    print(num3,"is largerst")        
