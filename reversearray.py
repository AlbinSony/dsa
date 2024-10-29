def reverse_array(i, arr, n):
    if i >= n // 2:
        return
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    reverse_array(i + 1, arr, n)

n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter array elements: ").split()))

reverse_array(0, arr, n)
print("Reversed array:", *arr)
