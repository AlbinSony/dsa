#include <iostream>
using namespace std;

bool checkArmstrong(int n){
	//Write your code here
	int ld,sum=0;
	int org=n;
	while(n>0){
		ld=n%10;
		sum=sum+(ld*ld*ld);
		n=n/10;
	}
	return (org==sum);
}

int main(){
	int n;
	cin>>n;
	if(checkArmstrong(n)){
		cout<<"true";
	}
	else{
		cout<<"false";
	}
	return 0;
}
