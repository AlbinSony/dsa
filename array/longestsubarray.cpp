#include<bits/stdc++.h>
int longestSubarrayWithSumK(vector<int> a, long long k) {
    map<long long, int> preSumMap;  // Map to store the prefix sum and its index
    long long sum = 0;             // Variable to keep track of the running sum
    int maxLen = 0;                // Variable to store the length of the longest subarray
    
    for (int i = 0; i < a.size(); i++) {
        sum += a[i];               // Add the current element to the running sum
        
        if (sum == k) {            // If the sum itself equals k
            maxLen = max(maxLen, i + 1);  // Update maxLen as the entire array so far forms the subarray
        }

        long long rem = sum - k;   // Calculate the remaining sum required to form sum = k
        if (preSumMap.find(rem) != preSumMap.end()) {  // Check if this sum exists in the map
            int len = i - preSumMap[rem];  // Calculate the length of the subarray
            maxLen = max(maxLen, len);    // Update maxLen
        }

        if (preSumMap.find(sum) == preSumMap.end()) {  
            // Store the first occurrence of this prefix sum
            preSumMap[sum] = i;         
        }
    }

    return maxLen;                 // Return the length of the longest subarray
}
