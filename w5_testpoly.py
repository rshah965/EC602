import unittest
import sys

# Author Rishab Shah rishah@bu.edu

from my_polynomial_solution import Polynomial
authors=['rishah@bu.edu']
class PolynomialTestCase(unittest.TestCase):
    """unit testing for polynomials"""

    def test_init(self):
	a=Polynomial()
	a[4]=0
	a[3]=1
	a[2]=2
	a[1]=3
	a[0]=-1
        self.assertIsInstance(a,Polynomial)
	self.assertNotEqual(a,Polynomial([1,2,3,-1]))

    def test_sparse_zeros(self):
        n = 10000
        p = Polynomial([0]*n)
        q = Polynomial()
        p_size =sum(sys.getsizeof(getattr(p,x)) for x in vars(p))
        q_size =sum(sys.getsizeof(getattr(q,x)) for x in vars(q))        
        factor_increase = p_size/q_size
        self.assertEqual(p,q)
        self.assertLess(factor_increase,10,msg='Implementation not sparse, init with {} zeros'.format(n))

    def test_add(self):
        p=Polynomial([2,12,1,45,11])
        q=Polynomial([3,1,1,1,-1])
	self.assertEqual(p+q,Polynomial([5,13,2,46,10]))
	self.assertEqual(p,Polynomial([2,12,1,45,11]))
	self.assertEqual(q,Polynomial([3,1,1,1,-1]))

    def test_sub(self):
        p=Polynomial([2,12,1,45,11])
        q=Polynomial([3,1,1,1,-1])
	self.assertEqual(p-q,Polynomial([-1,11,0,44,12]))
	self.assertEqual(p,Polynomial([2,12,1,45,11]))
	self.assertEqual(q,Polynomial([3,1,1,1,-1]))

    def Uneven_add(self):
        p=Polynomial([2])
        q=Polynomial([3,99,111,8781,-15616])
	self.assertEqual(p+q,Polynomial([3,99,111,8781,-15614]))
	self.assertEqual(p,Polynomial([2]))
	self.assertEqual(q,Polynomial([3,99,1111,8781,-15616]))

    def Uneven_sub(self):
        p=Polynomial([2])
        q=Polynomial([3,99,111,8781,-15616])
	self.assertEqual(p-q,Polynomial([-3,-99,-111,-8781,15618]))
	self.assertEqual(p,Polynomial([2]))
	self.assertEqual(q,Polynomial([3,99,1111,8781,-15616]))

    def test_mul(self):
        p=Polynomial([-1,2])
        p[-1]=5
        q=Polynomial([3,2,1,0,5,6])
        w=Polynomial([-3,4,18,12,0,4,37])
        w[-1]=30
        r=Polynomial([-1,2])
        r[-1]=5
        self.assertEqual(p*q,w)
        self.assertEqual(p,r)
        self.assertEqual(q,Polynomial([3,2,1,0,5,6]))

    def test_neg(self):
        p=Polynomial()
        p[-1000.0258963]=2
        self.assertEqual(p[-1000.0258963],2)

    def get_missing_key(self):
        x=Polynomial()
        self.assertEqual(x[2],4)

    def test_deriv(self):
        x=Polynomial([3,2,-5,-8.5,10.2])
        self.assertEqual(x.deriv(),Polynomial([12,6,-10,-8.5]))

    def test_eval(self):
        x=Polynomial([-10,1,3])
        self.assertAlmostEqual(x.eval(0.2),2.8)

    def get_key(self):
        x=Polynomial([3,2,1])
        x[-1.123142]=2143213
        x[-2]=0
        self.assertEqual(x[-1.123142],2143213)
        self.assertEqual(x[-2],0)
        self.assertEqual(x[1],2)      

    def test_eq(self):
        z = Polynomial()
        z[4]=3
        z[3]=5
        z[2]=1
        z[1]=1
        z[0]=2
        y=Polynomial([3,5,1,1,2])
        self.assertEqual(z==y,True)
        self.assertEqual(Polynomial([1,2])==Polynomial([3,1,2]),False)

if __name__ == '__main__':
    unittest.main()
