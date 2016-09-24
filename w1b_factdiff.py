# Author Rishab Shah rishah@bu.edu

import math
def fact(n): 
    if n == 0: 
        return 1 
    else: 
        return n * fact(n-1)
x=int(input ("Input a number"),10)
y=int(input ("Input a second number"),10)
if (x < 0 or y < 0):
    print('Please input positive numbers')
else:
    z=fact(x)-fact(y)
    print (z)
    #print(bin(z))
    if z<0:
        print(len(str(z))-1) 
    else:
        print(len(str(z)))
    p=z.bit_length()/8
#print (p)
    if isinstance(p,float):
        if p==0:
            print('1')
        else:
            p=math.ceil(p)
    print (p)
