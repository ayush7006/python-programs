num = int(input("enter number-->"))

# recurssion

def fact(a):
    if a == 0:
        return 1
    else :
        return (a*fact(a-1))

result = fact(num)
print(result)