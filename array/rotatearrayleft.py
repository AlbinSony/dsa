def rotateArray(arr: list, k: int) -> list:
    n = len(arr)  # Length of the array
    temp = [0] * k  # Initialize temp list with size k

    # Copy the first k elements to the temp list
    for i in range(k):
        temp[i] = arr[i]

    # Shift the remaining elements to the front
    for i in range(k, n):
        arr[i - k] = arr[i]

    # Copy the elements from temp back to the array
    for i in range(n - k, n):
        arr[i] = temp[i - (n - k)]

    return arr
