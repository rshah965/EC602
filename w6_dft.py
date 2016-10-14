# Author Rishab Shah rishah@bu.edu

from numpy import zeros,exp,array,pi

def DFT(x):
	X=zeros((len(x),))
	N=len(x)
	n=array(range(N))
	k=n[:,None]
	E=exp(-2j * pi * k * n / N)
	return sum(a*b for a,b in zip(E,x))
