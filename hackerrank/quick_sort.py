def quickSort(n:list):
    pivot = 0
    if len(n) <2:
        return n
    while True:
        p = 0
        q = 0
        for i in range(1, len(n)):
            if p == 0 and n[i] > n[pivot]:
                p = i
            if q == 0 and n[len(n)-i] < n[pivot]:
                q = len(n)-i
            if p != 0 and q != 0:
                break
        if p > q:
            temp = n[pivot]
            n[pivot] =n[q]
            n[q] = temp 
            pivot = q
            break
        else:
            temp = n[p]
            n[p] =n[q]
            n[q] = temp 
    left = quickSort(n[:pivot])
    right = quickSort(n[pivot+1:])
    return left + [n[pivot]] + right
print(quickSort([2,1,10,8, 7, 6,50,9, 100,3, 5,25,18, 17 ,19,13,40,50,38,23]))