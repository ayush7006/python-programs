def hcf(a,b):
    if a<b:
        smaller=a
    else:
        smaller=b

    for i in range(1,smaller+1):
        if (a%i==0) and (b%i==0):
            hcl=i
    return hcl


print(hcf(18,30))    