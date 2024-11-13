def sorted_array(a, b):
    n1 = len(a)
    n2 = len(b)
    i = 0
    j = 0
    union_arr = []

    while i < n1 and j < n2:
        if a[i] < b[j]:
            if len(union_arr) == 0 or union_arr[-1] != a[i]:
                union_arr.append(a[i])
            i += 1
        else:
            if len(union_arr) == 0 or union_arr[-1] != b[j]:
                union_arr.append(b[j])
            j += 1

    while i < n1:
        if len(union_arr) == 0 or union_arr[-1] != a[i]:
            union_arr.append(a[i])
        i += 1

    while j < n2:
        if len(union_arr) == 0 or union_arr[-1] != b[j]:
            union_arr.append(b[j])
        j += 1

    return union_arr
