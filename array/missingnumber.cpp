int missingNumber(vector<int>& a, int N) {
    int expected_sum = (N * (N +1)) / 2;
    int actual_sum = 0;
    for (int i = 0; i < N - 1; i++) {
        actual_sum += a[i];
    }
    return expected_sum - actual_sum;
}
