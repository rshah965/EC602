#include <iostream>
#include <ctime>
#include<cmath>

using namespace std;

// Author Rishab Shah rishah@bu.edu

int main()
{

    clock_t start_clock,end_clock;

    start_clock = clock();  // Timing starts here

    short unsigned int m=1;

    while (m>0)
        m++;

    end_clock = clock();    // Timing stops here

    double seconds = ((double)(end_clock-start_clock) / CLOCKS_PER_SEC )*1e6;

    cout << "short unsigned int time (microseconds): " << seconds  << endl;

    start_clock = clock();  // Timing starts here

    unsigned int m2=1;

    while (m2>0)
        m2++;

    end_clock = clock();    // Timing stops here

    double seconds2 = ((double)(end_clock-start_clock) / CLOCKS_PER_SEC );

    cout << "unsigned int time (seconds): " << seconds2  << endl;

    double seconds3= (seconds2*((pow(2,64)-1)/(pow(2,32)-1)))/(60*60*24*365);

    cout << "long unsigned int time (years): " << seconds3  << endl;
}
