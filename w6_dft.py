# Author Rishab Shah rishah@bu.edu

from numpy import zeros,exp,array,pi

def DFT(x):
	try:
		'''if (type(x) is dict or type(x) is str or type(x) is set or type(x) is frozenset or type(x) is function):
			raise ValueError('Input should be a sequence of values only.')'''
		for i in range(len(x)):
			if (type(x[i]) is tuple or type(x[i]) is list or type(x[i]) is dict or type(x[i]) is str):
				raise ValueError('Input should be a sequence of values only.')
		X=zeros((len(x),))
		N=len(x)
		n=array(range(N))
		k=n[:,None]
		E=exp(-2j * pi * k * n / N)
	except:
		raise ValueError
	return sum(a*b for a,b in zip(E,x))
