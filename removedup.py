def removeDuplicates(arr,n):
    # Write your code here.
    i=0
    for j in range(1,n):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1
    return i+1