def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    print("After sort:", arr)

n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for _ in range(n):
    element = int(input())
    arr.append(element)

insertion_sort(arr)
