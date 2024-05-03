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
