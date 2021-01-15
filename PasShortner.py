import functools
import operator
from itertools import permutations
f=open('Passs.txt','w+')
c=input("enter the sentence")
e=list(c.split())
for a in range(1,6):
     comb = permutations(e,a)
     for i in list(comb):
     	b= functools.reduce(operator.add, (i))
     	k= functools.reduce(operator.add, (b))
     	d=len(k)
     	if d<16 and d>7:
     		print(k)
     		f=open('Passs.txt','a')
     		f.write(k)
     		f.write('\n')
