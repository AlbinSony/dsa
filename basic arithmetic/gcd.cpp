#include <iostream>
using namespace std;

int main() {
    int n1, n2, gcd = 1;
    cout << "Enter 1st number: ";
    cin >> n1;
    cout << "Enter 2nd number: ";
    cin >> n2;

    for (int i = min(n1, n2); i >= 1; i--) {
        if (n1 % i == 0 && n2 % i == 0) {
            gcd = i;
            break;  // Exit the loop once the greatest divisor is found
        }
    }

    cout << "GCD is: " << gcd << endl;
    return 0;
}



//optimal
#include <iostream>
using namespace std;

int main() {
    int n1, n2, gcd = 1;
    cout << "Enter 1st number: ";
    cin >> n1;
    cout << "Enter 2nd number: ";
    cin >> n2;

    while(n1>0 && n2>0){
        if(n1>n2){
            n1=n1%n2;
        }
        else{
            n2=n2%n1;
        }
    }
    if(n1==0)
    cout<<n2;
    else{
        cout<<n1;
    }

    return 0;
}
