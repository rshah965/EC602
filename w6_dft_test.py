# Author Rishab Shah rishah@bu.edu

import unittest
import numpy as np

class DFTTestCase(unittest.TestCase):
	'''def test_return_Type(self):
		x=[1+2j,-5.026+0.3j,-9j,3]
		self.assertEqual(type(DFT(x)),type(np.fft.fft(x)))'''
	
	'''def test_return_Shape(self):
		x=(1,3-1j,5-0j)
		self.assertEqual(DFT(x).shape,np.fft.fft(x).shape)'''

	'''def test_invalid_Input_tuple(self):
		x=[2,4j,6.435234,(1,2,-4j)]
		self.assertRaises(ValueError,DFT,x)

	def test_invalid_Input_list(self):
		x=[2,4j,6.34,[1,0.26546j,-4j]]
		self.assertRaises(ValueError,DFT,x)

	def test_invalid_Input_dict(self):
		x=[2,4j,6.435234,{1:2,2:3,4:-4j}]
		self.assertRaises(ValueError,DFT,x)

	def test_invalid_Input_str(self):
		x=[2,'4j',6.435234,-8j,9+6j]
		self.assertRaises(ValueError,DFT,x)

	def test_invalid_Input_dict(self):
		x={1:255555555555,2:3,4:-4j}
		self.assertRaises(ValueError,DFT,x)'''

	'''def test_valid_Input_list(self):
		y=[]
		for i in range (2,21):
			x=np.random.uniform(-1,1,[i,])+1j*np.random.uniform(-1,1,[i,])
			for k in range(len(x)):
				y.append(x[j])
			for k in range(10):
				self.assertEqual(np.allclose(DFT(y),np.fft.fft(y)),True)

	def test_empty(self):
		self.assertIsInstance(DFT([1,3j]),np.ndarray)'''

	def test_invalid_Input_stror(self):
		x='gsdgf'
		self.assertRaises(ValueError,DFT,x)
	
	def test_bytearray(self):
		try:
			DFT(bytearray([1,2]))
		except:
			self.fail(None)
	
	def test_eq(self):
		for i in range (2,21):
			x=np.random.uniform(-1,1,[i,])+1j*np.random.uniform(-1,1,[i,])
			for k in range(10):
				self.assertEqual(np.allclose(DFT(x),np.fft.fft(x)),True)

if __name__ == '__main__':
	from w6_dft import DFT
	unittest.main()
