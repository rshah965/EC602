#include<vector>

// Author Rishab Shah rishah@bu.edu

using namespace std;

typedef vector<double> Poly;

// Add two polynomials, returning the result
Poly add_poly(const Poly &a,const Poly &b)
{
    int N;
    vector<double>A=a;
    vector<double>B=b;
    //vector<double>C;
    if (A.size()>B.size())
    {    N=A.size();
         while(A.size()>B.size())
            B.push_back(0);
    }
    else
    {    N=B.size();
         while(B.size()>A.size())
            A.push_back(0);
    }
    int i=0;
    while(i<N)
    {
        A[i]+=B[i];
        i=i+1;
    }
    return A;
}
// Multiply two polynomials, returning the result.
Poly multiply_poly(const Poly &a,const Poly &b)
{
    vector<double>A=a;
    vector<double>B=b;
    vector<double>C;
    vector<double>D;
    for(int i=0;i<A.size();i++)
    {
        for(int j=0;j<B.size();j++)
            C.push_back(A[i]*B[j]);
        B.insert(B.begin(),0);
        D=add_poly(C,D);
        C.clear();
    }
    return D;
}
