import unittest
import sys

# Author Rishab Shah rishah@bu.edu

from my_polynomial_solution import Polynomial
authors=['rishah@bu.edu']
class PolynomialTestCase(unittest.TestCase):
    """unit testing for polynomials"""


    def setUp(self):
        pass

    def test_init(self):
	a=Polynomial()
	a[3]=1
	a[2]=2
	a[1]=3
	a[0]=-1
        self.assertIsInstance(a,Polynomial)
	self.assertEqual(a,Polynomial([1,2,3,-1]))

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

    '''def long_add(self):
        p=Polynomial([2000000000000000000000000000000000000000000000000000000])
        q=Polynomial([3,95555555555555555555555555555555555555555559,111,8781,-15614])
	self.assertEqual(p+q,Polynomial([3,95555555555555555555555555555555555555555559,111,8781,1999999999999999999999999999999999999999999999999984386]))
	self.assertEqual(p,Polynomial([2000000000000000000000000000000000000000000000000000000]))
	self.assertEqual(q,Polynomial([3,95555555555555555555555555555555555555555559,1111,8781,-15614]))'''

    def Uneven_sub(self):
        p=Polynomial([2])
        q=Polynomial([3,99,111,8781,-15616])
	self.assertEqual(p-q,Polynomial([-3,-99,-111,-8781,15618]))
	self.assertEqual(p,Polynomial([2]))
	self.assertEqual(q,Polynomial([3,99,1111,8781,-15616]))

    '''def long_sub(self):
        p=Polynomial([2000000000000000000000000000000000000000000000000000000])
        q=Polynomial([3,95555555555555555555555555555555555555555559,111,8781,15614])
	self.assertEqual(p-q,Polynomial([-3,-95555555555555555555555555555555555555555559,-111,-8781,1999999999999999999999999999999999999999999999999984386]))
	self.assertEqual(p,Polynomial([2000000000000000000000000000000000000000000000000000000]))
	self.assertEqual(q,Polynomial([3,95555555555555555555555555555555555555555559,1111,8781,15614]))'''

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

    '''def test_longmul(self):
        x=Polynomial([6666,555555555,444444,77,2.2222222222222,58,6151484984898484])
        p=Polynomial()
        p[1950000]=-3
	p[194000]=2.5
	p[19548948161498418953]=17
	p[0]=12451651651651519
        p[-1.5]=516
        q=p*x
        r=Polynomial([83002709909909025654L,6917584243999926304638045L,5534061866666607710436L,958777177177166963,2.767033700366977e+16,722195795795788102,76596148172320727711873159397196L])
        r[19548948161498418953L]= 104575244743274228
        r[19548948161498418954L]= 986
        r[19548948161498418955L]= 37.7777777777774
        r[19548948161498418956L]= 1309
        r[19548948161498418957L]= 7555548
        r[19548948161498418958L]= 9444444435
        r[19548948161498418959L]= 113322
        r[0.5]= 1146.6666666666551
        r[-0.5]= 29928
        r[1950000]= -18454454954695452
        r[1950001]= -174
        r[1950002]= -6.6666666666666
        r[1950003]= -231
        r[1950004]= -1333332
        r[1950005]= -1666666665
        r[1950006]= -19998
        r[-1.5]= 3174166252207617744
        r[1.5]= 39732
        r[194000]= 1.537871246224621e+16
        r[194001]= 145.0
        r[194002]= 5.5555555555555
        r[194003]= 192.5
        r[194004]= 1111110.0
        r[194005]= 1388888887.5
        r[194006]= 16665.0
        r[2.5]= 229333104
        r[3.5]= 286666666380
        r[4.5]= 3439656
        self.assertEqual(q,r)'''   

    def tearDown(self):
        "tear down"

if __name__ == '__main__':
    unittest.main()
