// AUTHOR Rishab Shah rishah@bu.edu

#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;


typedef vector< vector<int> > int_m;
typedef vector< vector<double> > double_m;

int_m mul(int_m A, int_m B){
    
    int M = A.size();
    int N = A[0].size();
    int L = B[0].size();
    int sum = 0;
    
    int_m c(M);
    
    for (int i=0;i<M;i++)
    for (int j=0;j<L;j++)
    for (int n=0;n<N;n++){
        sum = sum + (A[i][n]*B[n][j]);
        if (n == (N-1)){
            c[i].push_back(sum);
            sum = 0;
        }
    }
    return c;
    
}

double_m double_mul(double_m A, double_m B){
    
    int M = A.size();
    int N = A[0].size();
    int L = B[0].size();
    double sum = 0;
    
    double_m c(M);
    
    for (int i=0;i<M;i++)
    for (int j=0;j<L;j++)
    for (int n=0;n<N;n++){
        sum = sum + (A[i][n]*B[n][j]);
        if (n == (N-1)){
            c[i].push_back(sum);
            sum = 0;
        }
    }
    return c;
    
}



int main (int argc, char const *argv[])
{
    int M, N, L, i;
    string s1,s2,s3,s4,s5,s6,s7;
    if(argc!=8 && argc !=6 ){
        return 1;
    }
    if(argc == 8){
        s1 = argv[1];
        
        s2 = argv[2];
        s3 = argv[3];
        s4 = argv[4];
        
        s5 = argv[5];
        s6 = argv[6];
        s7 = argv[7];
    }
    
    if(argc == 6){
        s1 = argv[1];
        
        s2 = argv[2];
        s3 = argv[2];
        s4 = argv[2];
        
        s5 = argv[3];
        s6 = argv[4];
        s7 = argv[5];
    }
    
    M = atoi(s2.c_str());
    N = atoi(s3.c_str());
    L = atoi(s4.c_str());
    //cout<<M<<" "<<N<<" "<<L<<endl;
    if(s1!="int" && s1!="double" ){
        return 1;
    }
    
    if(M<=0 || N<=0 || L<=0 ){
        return 1;
    }
    
    //cout<<d<<endl;
    
    if(s1== string("int")){
        vector<vector <int> > A(M);
        vector<vector <int> > B(N);
        ifstream thisfile; // note: this is an IFSTREAM, "I" stands for INPUT
        
        int one;
        
        
        thisfile.open(s5);
        if (thisfile.fail()==1){
            return 2;
        }
        i = 0;
        
        while (thisfile >> one)
        {
            i++;
        }
        
        thisfile.close();
        if (i != (M*N)){
            return 3;
        }
        thisfile.open(s6);
        if (thisfile.fail()==1){
            return 2;
        }
        i = 0;
        
        while (thisfile >> one)
        {
            i++;
        }
        
        thisfile.close();
        if (i != (N*L)){
            return 3;
        }
        
        thisfile.open(s5);
        
        for (i = 0; i < M; i++){
            for (int j = 0; j < N; j++){
                thisfile >> one;
                A[i].push_back(one);
            }
        }
        thisfile.close();
        
        thisfile.open(s6);
        
        for (i = 0; i < N; i++){
            for (int j = 0; j < L; j++){
                thisfile >> one;
                B[i].push_back(one);
            }
        }
        
        thisfile.close();
        
        int_m C = mul(A, B);
        
        ofstream filewithnumbers; // note: this is an OFSTREAM, "O" stands for OUTPUT
        
        filewithnumbers.open(s7);
        if(filewithnumbers.is_open() == 0){
            return 4;
        }
        for (i=0; i < M; i++){
            for(int j = 0; j < L; j++){
                filewithnumbers <<C[i][j]<<" ";
                if (j == L - 1){
                    filewithnumbers << endl;
                }
            }
        }
        
        filewithnumbers.close();
    }
    else{
        vector<vector <double> > A(M);
        vector<vector <double> > B(N);
        ifstream thisfile; // note: this is an IFSTREAM, "I" stands for INPUT
        
        double one;
        
        
        thisfile.open(s5);
        if (thisfile.fail()==1){
            return 2;
        }
        i = 0;
        
        while (thisfile >> one)
        {
            i++;
        }
        
        thisfile.close();
        if (i != (M*N)){
            return 3;
        }
        thisfile.open(s6);
        if (thisfile.fail()==1){
            return 2;
        }
        i = 0;
        
        while (thisfile >> one)
        { 
            i++;
        }
        
        thisfile.close();
        if (i != (N*L)){
            return 3;
        }
        
        thisfile.open(s5);
        
        for (i = 0; i < M; i++){
            for (int j = 0; j < N; j++){
                thisfile >> one;
                A[i].push_back(one);
            }
        }
        thisfile.close(); 
        
        thisfile.open(s6);
        
        for (i = 0; i < N; i++){
            for (int j = 0; j < L; j++){
                thisfile >> one;
                B[i].push_back(one);
            }
        }
        
        thisfile.close();
        
        double_m C = double_mul(A, B);
        
        ofstream filewithnumbers; // note: this is an OFSTREAM, "O" stands for OUTPUT
        
        filewithnumbers.open(s7);
        if(filewithnumbers.is_open() == 0){
            return 4;
        }
        for (i=0; i < M; i++){
            for(int j = 0; j < L; j++){
                filewithnumbers <<C[i][j]<<" ";
                if (j == L - 1){
                    filewithnumbers << endl;
                }
            }
        }
        
        filewithnumbers.close();
    }
    return 0;
}
