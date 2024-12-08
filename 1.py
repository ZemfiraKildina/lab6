from itertools import *
k=0
a = 'НАСТЯ'
for i in product(a,repeat=6):
    s=''.join(i)
    if s.count('А')<=1 and s.count('Я')<=1:
        k+=1
print(k)
