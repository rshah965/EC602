// Author Rishab Shah rishah@bu.edu
#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main(int argc, char const *argv[])
{
    int M,N,L;
    string s3,s4,s5;
    ifstream thisfile;
    double one,two;
    //string s1(argv[0]);
    string s2(argv[1]);
    if (argc ==6 || argc == 8){
    if (argc==6){
        M=stoi(argv[2]);
        N=M;
        L=M;
        s3=string(argv[3]);
        s4=string(argv[4]);
        s5=string(argv[5]);
        }
    else if (argc==8){
        M=stoi(argv[2]);
        N=stoi(argv[3]);
        L=stoi(argv[4]);
        s3=string(argv[5]);
        s4=string(argv[6]);
        s5=string(argv[7]);
    }
    }
    else{
        cout << "213" << endl;
        return 1;}
    if (M<=0 || N<=0 || L<=0){
        return 1;}
    ofstream thisfile2;
    thisfile2.open(s5);
    if (thisfile2.is_open()==0){
        cout<<"123123"<<endl;
        return 4;}
    thisfile2.close();
    //cout << M << N << L << s3 << s4 << s5 <<endl;
    if (s2 != "int" && s2 != "double"){
        //cout << "going in this loop" <<endl;
        return 1;}
    if (s2=="int"){
    vector<vector<int> > A(M, vector<int>(N));
    vector<vector<int> > B(N, vector<int>(L));
    ifstream f(s3);
    if (f.good() == true){
        //cout << "nice" << endl;
        thisfile.open(s3);
        int cnt = 0;
        while(thisfile >> one){
            cnt=cnt+1;
        }
        thisfile.close();
        thisfile.open(s3);
        if (cnt == M*N){
            //cout << "going in loop" << M << N << endl;
            while (thisfile >> two){
                for (int i=0; i<M; ++i){
                    for (int j=0;j<N;++j){
                        A[i][j]=two;
                        thisfile >> two;
                        //cout << "i " << i << " j " << j << " val " << A[i][j] << endl;
                    }
                }
            }
        }
        else{
            return 3;}
            //cout << "wrong index" << endl;}
        thisfile.close();}
    else {
        return 2;}
        //cout << "file does not exist" << endl;}


    ifstream f2(s4);
    if (f2.good() == true){
        //cout << "nice" << endl;
        thisfile.open(s4);
        if(thisfile.good() == true){}
        int cnt = 0;
        while(thisfile >> one){
            cnt=cnt+1;
        }
        thisfile.close();
        thisfile.open(s4);
        if(thisfile.good() == true){}
        if (cnt == N*L){
            //cout << "going in loop" << N << L << endl;
            while (thisfile >> two)
            {
                for (int i=0; i<N; ++i){
                    for (int j=0;j<L;++j){
                        B[i][j]=two;
                        thisfile >> two;
                        //cout << "i " << i << " j " << j << " val " << B[i][j] << endl;
                    }
                }
            }
        }
        else{
            return 3;}
            //cout << "wrong index" << endl;}
        thisfile.close();}
    else{
        return 2;}
        //cout << "file does not exist" << endl;}


        int l= B[0].size();
        int m=A.size();
        int n=A[0].size();
        vector<vector<int> > c(m,vector<int>(l));
        for (int i=0;i<m;i++)
            for (int j=0;j<l;j++)
                for (int k=0;k<n;k++)
                    c[i][j] += A[i][k] * B[k][j];
        ofstream xyz;
        xyz.open(s5);
        for (int i=0;i<m;i++)
            for (int j=0;j<l;j++){
                //cout << c[i][j] << endl;
                xyz << c[i][j] << endl;}
        xyz.close();
    }
    if (s2=="double"){
    vector<vector<double> > A(M, vector<double>(N));
    vector<vector<double> > B(N, vector<double>(L));
    ifstream f(s3);
    if (f.good() == true){
        //cout << "nice" << endl;
        thisfile.open(s3);
        int cnt = 0;
        while(thisfile >> one){
            cnt=cnt+1;
        }
        thisfile.close();
        thisfile.open(s3);
        if (cnt == M*N){
            //cout << "going in loop" << M << N << endl;
            while (thisfile >> two){
                for (int i=0; i<M; ++i){
                    for (int j=0;j<N;++j){
                        A[i][j]=two;
                        thisfile >> two;
                        //cout << "i " << i << " j " << j << " val " << A[i][j] << endl;
                    }
                }
            }
        }
        else{
            return 3;}
            //cout << "wrong index" << endl;}
        thisfile.close();}
    else {
        return 2;}
        //cout << "file does not exist" << endl;}


    ifstream f2(s4);
    if (f2.good() == true){
        //cout << "nice" << endl;
        thisfile.open(s4);
        if(thisfile.good() == true){}
        int cnt = 0;
        while(thisfile >> one){
            cnt=cnt+1;
        }
        thisfile.close();
        thisfile.open(s4);
        if(thisfile.good() == true){}
        if (cnt == N*L){
            //cout << "going in loop" << N << L << endl;
            while (thisfile >> two)
            {
                for (int i=0; i<N; ++i){
                    for (int j=0;j<L;++j){
                        B[i][j]=two;
                        thisfile >> two;
                        //cout << "i " << i << " j " << j << " val " << B[i][j] << endl;
                    }
                }
            }
        }
        else{
            return 3;}
            //cout << "wrong index" << endl;}
        thisfile.close();}
    else{
        return 2;}
        //cout << "file does not exist" << endl;}


        int l= B[0].size();
        int m=A.size();
        int n=A[0].size();
        vector<vector<double> > c(m,vector<double>(l));
        for (int i=0;i<m;i++)
            for (int j=0;j<l;j++)
                for (int k=0;k<n;k++)
                    c[i][j] += A[i][k] * B[k][j];
        ofstream xyz;
        xyz.open(s5);
        for (int i=0;i<m;i++)
            for (int j=0;j<l;j++){
                //cout << c[i][j] << endl;
                xyz << c[i][j] << endl;}
        xyz.close();
    }
    return 0;
}
