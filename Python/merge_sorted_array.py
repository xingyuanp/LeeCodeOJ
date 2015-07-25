def merge(A, m, B, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    if i < 0:
        A[:j+1] = B[:j+1]
        