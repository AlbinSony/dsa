#include <iostream>
using namespace std;

void print(int i,int num) {
    if(i>num){
        return;
    }
    cout<<"ALBIN";
    cout<<endl;
    print(i+1,num);
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    print(1,n);
    return 0;
}
