def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]  # Swapping elements

n = int(input("Enter number of elements: "))
arr = [int(input()) for _ in range(n)]

selection_sort(arr)
print("Sorted array:", arr)
