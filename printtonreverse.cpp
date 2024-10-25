#include <iostream>
using namespace std;

void print(int num) {
    if (num < 1) {
        return;
    }
    cout << num << endl;
    print(num - 1);
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    print(n);
    return 0;
}
