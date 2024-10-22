#include <iostream>
using namespace std;

bool palindrome(int n) {
    int ld, rev = 0;
    int org = n;

    while (n > 0) {
        ld = n % 10;
        rev = (rev * 10) + ld;
        n = n / 10;
    }

    return rev == org;
}

int main() {
    int n;
    cin >> n;

    if (palindrome(n)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }

    return 0;
}
