#include<vector>
using namespace std;
int getSingleElement(vector<int> &arr){
	int maxi=0;
	for(int i=0;i<arr.size();i++){
		maxi=max(maxi,arr[i]);
	}
	vector<int>hash(maxi+1,0);
	for(int i=0;i<arr.size();i++){
		hash[arr[i]]++;
	}
	for(int i=0;i<arr.size();i++){
		if(hash[arr[i]]==1){
			return arr[i];
		}
	}

	return -1;
}

