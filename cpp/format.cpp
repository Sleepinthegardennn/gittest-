/*
 * format.cpp
 * 
 */

#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdio>


using namespace std;
 
int main(int argc, char **argv)
{
	int li = 100;
    float lf = 12.678;
    
    printf("%10.4f\n", M_PI);
    printf("%10.4f\n", lf);
    printf("%10.4f\n", (double)li);
    printf("%10.4d\n", li);
    printf("%10d\n", li);
    printf("Hex: %#x\n", li);
    printf("Oct: %#o\n", li);
    
    cout.precision(5);
    cout.width(20);
    cout << lf << endl;
    cout << setprecision(5) << setw(20) << M_PI << endl;
    cout << hex << li << endl;
    cout << oct << li << endl;
	return 0;
}

