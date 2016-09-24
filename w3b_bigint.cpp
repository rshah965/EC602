#include<string>
#include<vector>

using namespace std;

// Author Rishab Shah rishah@bu.edu

typedef string BigInt;

typedef vector<unsigned long long int> Poly;

// Add two polynomials, returning the result
Poly add_poly(const Poly &a,const Poly &b)
{
    int N;
    vector<unsigned long long int>A=a;
    vector<unsigned long long int>B=b;
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
    vector<unsigned long long int>A=a;
    vector<unsigned long long int>B=b;
    vector<unsigned long long int>C;
    vector<unsigned long long int>D;
    for(unsigned int i=0;i<A.size();i++)
    {
        for(unsigned int j=0;j<B.size();j++)
            C.push_back(A[i]*B[j]);
        B.insert(B.begin(),0);
        D=add_poly(C,D);
        C.clear();
    }
    return D;
}


BigInt multiply_int(const BigInt &a,const BigInt &b)
{
      string A=a;
      char c;
      string B=b;
      char z='0';
      string x;
      int m;
      vector<unsigned long long int>p;
      vector<unsigned long long int>q;
      vector<unsigned long long int>r;
      vector<unsigned long long int>s;
      for (unsigned int i=0;i<A.length();i++)
      {
        c=A[i];
        p.push_back(c-z);
      }
      for (unsigned int k=0;k<B.length();k++)
      {
        c=B[k];
        q.push_back(c-z);
      }
      r=multiply_poly(p,q);
      for(unsigned int f=0;f<r.size();f++)
        s.insert(s.begin(),r[f]);
      for(unsigned int j=0;j<s.size();j++)
      {
        if (s.size()==1)
            break;
        if(s[j]>9)
        {
            m=s[j]/10;
            s[j]%=10;
            if (j==s.size()-1)
                s.insert(s.end(),m);
            else
                s[j+1]+=m;
        }
      }
      r.clear();
      for(unsigned int f=0;f<s.size();f++)
        r.insert(r.begin(),s[f]);
      for(unsigned int l=0;l<r.size();l++)
        x+=to_string(r[l]);
      return x;
}
