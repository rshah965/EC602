#Author Rishab Shah rishah@bu.edu

from itertools import permutations
from collections import Counter
while(1):
    x=input()
    y=x.split()
    z=int(y[1])
    with open ('big_wordlist.txt') as f:
        il=f.read().split()
    d={}
    for i in range(21):
        d[i]=[]
    for i in range(21):
        for j in range(len(il)):
            if (len(il[j])==i):
                d[i].append(il[j])
    
    if z<=8:
        d[z]=set(d[z])
        w={''.join(i) for i in permutations(y[0],z)}
        match=d[z] & w
        print(match)
    else:
        a=Counter(y[0])
        for i in range(len(d[z])):
            if (len(a&Counter(d[z][i]))==z):
                #d[z]=set(d[z])
                print(d[z])