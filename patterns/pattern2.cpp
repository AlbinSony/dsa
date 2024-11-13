// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
int printPattern(int n){
    int i,j;
    for(i=0;i<n;i++){
        for(j=0;j<=i;j++){
            cout<<"* ";
        }
        cout<<endl;
    }
    return 0;
}

int main() {
    int num;
    cout<<"enter number of rows: ";
    cin>>num;
    printPattern(num);
    return 0;
}