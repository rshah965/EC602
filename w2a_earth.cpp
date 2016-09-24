#include<iostream>
#include<math.h>

using namespace std;

// Author Rishab Shah rishah@bu.edu
int main()
{
    double M=5.97237*pow(10,24);
    double mu=3.9525627*pow(10,-25);
    double eu=92;
    double lb=((M/mu)*eu)/(8*1.09951162778*pow(10,12))/2;
    double mh=1.6737236*pow(10,-27);
    double eh=1;
    double ub=((M/mh)*eh)/(8*1.09951162778*pow(10,12))*1.5;
    double mfe=9.273796*pow(10,-26);
    double pfe=.321;
    double efe=26;
    double mo=2.6567626*pow(10,-26);
    double po=.301;
    double eo=8;
    double msi=4.6637066*pow(10,-26);
    double psi=.151;
    double esi=14;
    double mmg=4.0359398*pow(10,-26);
    double pmg=.139;
    double emg=12;
    double ms=5.3245181*pow(10,-26);
    double ps=.029;
    double es=16;
    double mni=9.7462675*pow(10,-26);
    double pni=.018;
    double eni=28;
    double mca=6.6551079*pow(10,-26);
    double pca=.015;
    double eca=20;
    double mal=4.4803895*pow(10,-26);
    double pal=.014;
    double eal=13;
    double mna=3.8175407*pow(10,-26);
    double pna=.012;
    double ena=11;
    double mass[]={mfe,mo,msi,mmg,ms,mni,mca,mal,mna};
    double percent[]={pfe,po,psi,pmg,ps,pni,pca,pal,pna};
    double elec[]={efe,eo,esi,emg,es,eni,eca,eal,ena};
    double avg=0.0;
    for (int i=0; i<9; i++)
        {
            avg+=((M/mass[i])*(percent[i]*elec[i]))/(8*1.09951162778*pow(10,12))*1.2;
        }
    cout << avg << endl;
    cout << lb << endl;
    cout << ub << endl;
}
