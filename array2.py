from turtle import clear


heros=['spider man','thor','hulk','iron man','captain america']
print('1. length of heros',+ len(heros))
print(heros)
heros.append('black panther')
print('2.after add  length of heros',+ len(heros))
print(heros)
heros.remove('hulk')
print(heros)
heros.append('hulk')
print(heros)
heros.remove('hulk')
heros.remove('thor')
heros.append('doctor strange')
print(heros)
heros.sort()
print(heros)