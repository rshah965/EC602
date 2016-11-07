// Show the command line argument values.
#include <iostream>
#include <string> // provides stoX where X can be i (int), d (double), etc.
#include<typeinfo>
#include <vector>
#include <fstream>

using namespace std;

//template <typename T>
//inline T const& mat_mul ( vector<vector<T> > const& A, vector<vector<T> > const& B){
//
// T M = A.size();
// T N = A[0].size();
// T L = B[0].size();
//
// vector<vector<T> > c(M,vector<T>(L));
//
// for (int i=0;i<M;i++)
//    for (int j=0;j<L;j++)
//        for (int k=0;k<N;k++){
//            c[i][j] += A[i][k] * B[k][j];
//            cout << c[i][j] << endl;}
//
// return c;
//}


int main(int argc, char const *argv[])
{
    // the following example shows what argc and argv are
    //
    // c-strings are hard to use properly and are dangerous.
//    int i,j;
//
//    cout << "argc is " << argc << endl;
    for (int i=0; i<argc; i++){
//        //print out argv[i]
//
        cout << "argv of " << i << " is " << argv[i] << " " << typeid(argv[i]).name() << endl;}
//
//        //print out argv[i], discover its length
//        j=0;
//        while ( argv[i][j])  // equivalent to (argv[i][j] != '\0')
//             cout << argv[i][j++];
//
//        cout << " len " << j;
//
//        // alternative
//        string s(argv[i]);
//        cout << typeid(s).name() << endl;
//        if (s == "w8c_multiply")
//        {
//            cout << "right" << endl;
//            //return 1;
//        }
//        else{
//            cout << "not yet or passed" ;
//        }
//        cout << " len " << s.size();
//        cout << endl;

    //if (argv[7]  || argv[9] == true){
        string s1(argv[1]);
        string s2(argv[2]);
        string s3(argv[5]);
        if (s1 != "w8c_multiply" || s2 != "int" && s2 != "double"){
            cout << "going in this loop" <<endl;
            return 1;}

        //else{
          //  return 1; }
//        if (argc == 6){
//            if ()}
   // }

        ifstream thisfile; // note: this is an IFSTREAM, "I" stands for INPUT
        double one,two;
        int M=stoi(argv[3]);
        int N=stoi(argv[4]);
        cout << M*N << endl;
        vector<vector<double> > matrix(M, vector<double>(N));
        ifstream f(s3);
        if (f.good() == true){
            cout << "nice" << endl;}
        else {
            cout << "file does not exist" << endl;}
        thisfile.open(s3);
            if(thisfile.good() == true){}
            int cnt = 1;
                while(thisfile >> one){
                    //cout << cnt << endl;

                    cnt=cnt+1;
                }
                thisfile.close();
                thisfile.open(s3);
                if(thisfile.good() == true){}
                cnt=cnt-1;
                cout << cnt << endl;
                if (cnt == M*N){
                    cout << "going in loop" <<endl;
                    while (thisfile >> two)
                    {
                        for (int i=0; i<M; ++i){
                            for (int j=0;j<N;++j){
                    //cout << one << " " << two << " ";
                                matrix[i][j]=two;
                                thisfile >> two;
                                cout << "i " << i << " j " << j << " val " << matrix[i][j] << endl;
                            }
                        }
//        for (int p=0;p<squares.size();++p)
//            cout << squares[p] << endl;
                    }
                }
                else{
                    cout << "wrong index" << endl;}
                thisfile.close();
    int L= matrix[0].size();
    int m=matrix.size();
    int n=matrix[0].size();
    vector<vector<double> > c(m,vector<double>(L));
    for (int i=0;i<m;i++)
        for (int j=0;j<L;j++)
            for (int k=0;k<n;k++)
                c[i][j] += matrix[i][k] * matrix[k][j];
    ofstream xyz;
    xyz.open("xyz.txt");
    for (int i=0;i<m;i++)
        for (int j=0;j<L;j++){
            cout << c[i][j] << endl;
            xyz << c[i][j] << endl;}
    xyz.close();
    return 0;
}
