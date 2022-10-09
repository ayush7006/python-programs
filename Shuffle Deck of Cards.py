import random as r
import itertools as it
deck = list(it.product(range(1,14),["spade","club","hearts","dimond"]))
r.shuffle(deck)
print(deck)
for itme in range(5):
    print(deck[itme][0],"of",deck[itme][1])