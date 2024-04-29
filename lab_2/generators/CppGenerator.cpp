/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <random>

using namespace std;

#define NUMBER_BITS 128

int random(int a, int b) {
    random_device random_device;
    mt19937 generator(random_device());
    uniform_int_distribution<> distribution(a, b);
    return distribution(generator);
}


int main() {
    for (int i = 0; i < NUMBER_BITS; i++) {
        cout << random(0, 1);
    }
    return 0;
}
