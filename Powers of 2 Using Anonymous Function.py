#lambda
n = int(input('enter your num-->'))
t = int(input('enter your times-->'))
sum = list(map(lambda i : n**i , range(t+1)))

for l in sum:
    print(l)