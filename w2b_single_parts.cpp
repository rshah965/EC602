// double_parts
#include <iostream>
#include <iomanip>
#include <cassert>

// Author Rishab Shah rishah@bu.edu
// Author Qifan He heqf@bu.edu

using namespace std;

typedef unsigned int raw64; // raw64 is a pseudonym for unsigned long long int

// A structure which mimics exactly the internal representation of double
// Double Parts uses  64-bits of storage

struct Single_Parts {
    raw64 fraction : 23;  // use 52 bits for this
    raw64 exponent : 8; // then 11 bits for this
    raw64 sign : 1;      // then 1 bit for this
} ;


// these represent the positions of the SIGN, EXPONENT, and FRACTION of double.

const raw64 MASK_SIGN = 1 << 31;
const raw64 MASK_BEXP = 0xff << 23;
const raw64 MASK_FRAC = 0x7fffff;


// print out the parts of the structure Double_Parts
void print_sp(Single_Parts sp)
{
  if (sp.sign==1)
         cout << "negative"  << endl;
  else
        cout << "positive" << endl;

 cout << hex
      << setfill('0')
      << "expo: " << sp.exponent << endl
      << "frac: " << sp.fraction << endl
      << dec;
}


// build and take_apart are inverse functions.

Single_Parts take_apart(float d)
{
 Single_Parts sp;
 raw64 x =  *reinterpret_cast<raw64*>(&d);

 sp.sign = (x bitand MASK_SIGN) >> 31;
 sp.exponent = (x bitand MASK_BEXP) >> 23;
 sp.fraction = (x bitand MASK_FRAC);

 return sp;

}

float build(Single_Parts sp)
{
       // read this from inside out:
       // this means get the address of dp, then think of it as a pointer to a double
       // then get the double and return it.
       return *reinterpret_cast<float*>(&sp);
}

float build_alt(Single_Parts sp)
{
    raw64 c=0;

    // explicitly move the double parts to their correct locations, and add.

    c = ( (raw64)sp.sign << 31) + ( (raw64)sp.exponent << 23) + sp.fraction;

    // read this from inside out:
    // this means get the address of c, then think of it as a pointer to a double
    // then get the double and return it.
    return *reinterpret_cast<float*>(&c) ;
}


// We will show 5 examples
//const int EXAMPLES = 5;

int main()
{
    assert(sizeof(raw64)==4); // make sure this is actually an 8-byte object.

    float num_from_build, num_from_build_alt;

    float numbers[5]={1.0/3,2,1.3e10,3e11,6};

    // show the structure of the numbers
    for (int i=0;i<5;i++)
    {
        // take apart the numbers, then re-build to test that it works.

        Single_Parts sp= take_apart(numbers[i]);
        num_from_build = build(sp);
        num_from_build_alt = build_alt(sp);

        cout << endl;
        print_sp(sp);
        cout << numbers[i] << " " << num_from_build << " " << num_from_build_alt << endl;
    }

    // example of a weird number, negative zero.
    /*float neg_zero{-0.0};

    cout << endl;
    cout << neg_zero << endl;

    print_sp(take_apart(neg_zero));*/

    return 0;
}


