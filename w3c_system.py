import numpy as np

# Author Rishab Shah rishah@bu.edu

x=input()
h=input()
xlist=[float(a) for a in x.split()]
hlist=[float(b) for b in h.split()]
y=np.convolve(xlist,hlist)
op=''
for c in range(len(y)-1):
	op+= str(y[c])+ ' '
op+=str(y[-1])
print(op)
