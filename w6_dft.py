# Author Rishab Shah rishah@bu.edu

#from numpy import zeros,exp,array,pi

#def DFT(x):
x=[-5-8j,4.020220,2,1,2-5j,6j,7j,2]
if (type(x) is "complex" or "int" or "float"):
	z=list()
	z.append(x)
	#X=zeros((1,))
for i in range(len(x)):
	print(i,type(x[i]))
	if (type(x[i]) is tuple or type(x[i]) is list or type(x[i]) is dict or type(x[i]) is str):
		print(type(x[i]))
		raise ValueError('Input should be a sequence of values only.')
print(x)
print(type(x))
print(type(x[0]))
'''X=zeros((len(x),))
N=len(x)
n=array(range(N))
k=n[:,None]
E=exp(-2j * pi * k * n / N)
print(sum(a*b for a,b in zip(E,x)))'''
	#return sum(a*b for a,b in zip(E,x))
