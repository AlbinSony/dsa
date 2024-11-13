#include<iostream>
using namespace std;

int main() {
    int n, ld, revNum = 0;
    cout << "Enter a number: ";
    cin >> n;
    while (n > 0) {
        ld = n % 10;
        revNum = (revNum * 10) + ld;
        n = n / 10;
    }
    cout << "Reversed Number: " << revNum << endl;
    return 0;
}
