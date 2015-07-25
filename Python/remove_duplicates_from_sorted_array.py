def removeDuplicates(A):
    if A == []:
        return 0
        
    i = 0
    for j in range(len(A)):
        if A[i] != A[j]:
            A[i + 1] = A[j]
            i += 1
    return i + 1
        
        