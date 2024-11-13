def bubble_sort(arr):
    n = len(arr)
    # bubble sort
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("After Using bubble sort:")
    for i in arr:
        print(i, end=" ")
    print()

# Main
arr = [13, 46, 24, 52, 20, 9]
print("Before Using Bubble Sort:")
print(" ".join(map(str, arr)))

bubble_sort(arr)
