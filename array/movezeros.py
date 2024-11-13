def moveZeros(n, a):
    # Find the first zero in the array
    j = -1
    for i in range(n):
        if a[i] == 0:
            j = i
            break
    if j == -1:
        return a
    for i in range(j + 1, n):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i] 
            j += 1

    return a
