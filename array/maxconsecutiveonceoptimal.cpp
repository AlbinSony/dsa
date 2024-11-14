#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int getSingleElement(vector<int>& arr) {
    unordered_map<int, int> mpp;
    for (int i = 0; i < arr.size(); i++) {
        mpp[arr[i]]++;
    }
    for (auto it : mpp) {
        if (it.second == 1) {
            return it.first;
        }
    }
    
    return -1;
}