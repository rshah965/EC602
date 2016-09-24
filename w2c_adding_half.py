# w2c_addinghalf.py
import math
from math import inf
# Author Rishab Shah rishah@bu.edu
def number_from_half(s: str):
 #   """return the number represented by s, a binary16 stored as a 4-character hex number"""
	x=int(s,16)	
	sign= x&0x8000
	sign=sign>>15
	#print(sign)
	exp=x&0x7c00
	exp=exp>>10
	#print(exp)
	frac=x&0x3ff
	#print(frac)
	m=list()
	mult=m
	v=list()
	r=v
	if exp in range(1,31):	
		u=1
		for i in range (0,10):			
			w=u&frac
			u=u<<1
			if i>0:
				w=w>>i
			m.append(w)
			#mult.reverse()
			#print(mult)
		for j in range (1,11):
			v.append(((2**(-j))*mult[10-j]))
	#print(mult[j])
		#print(r)	
		t= sum(r)
		#print(t)
		if sign>0:	
			z=-(2**(exp-15))*(1+t)
		else:
			z=(2**(exp-15))*(1+t)
		#print(z)
	elif exp == 0:
		u=1
		for i in range (0,10):			
			w=u&frac
			u=u<<1
			if i>0:
				w=w>>i
			m.append(w)
			#mult.reverse()
			#print(mult)
		for j in range (1,11):
				v.append(((2**(-j))*mult[10-j]))
			#print(mult[j])
		#print(r)	
		t=sum(r)
		#print(t)
		if sign>0:	
			z=-(2**(-14))*t
		else:
			z=(2**(-14))*t
		#print(z)

	else:
		if sign>0:
			z=-math.inf
		else:
			z=math.inf
		#print(z)	
	return z

def main():
	result=0
	y=list()	
	z=y
	try:
		while (math.ceil(result) > -65505 and math.ceil(result) < 65505):
			x=input()
			if (x == 'exit'):
				break
			else:									
				y.append(number_from_half(x))
				#print(z)
				result=sum(z)
				#print(math.ceil(result))
				#if (result == inf or result == -inf):
				#	break		
			if (math.ceil(result) < -65504):
				result=-math.inf
			if (math.ceil(result) > 65504):
				result=math.inf
		print(result)
				#print(number_from_half(x))
	except (ValueError,OverflowError):
		print('exit: Overflow or Value error')

if __name__ == '__main__':
    main()
