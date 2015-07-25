def removeElement(A, elem):
    """Given an array and a value, remove all instances of that value in place
    and return the new length. The order of elements can be changed. It doesn't
    matter what you leave beyond the new length.
    
    A: a list of integers
    elem: an integer, value need to be removed
    return an integer"""

    length = len(A)
    i = 0
    while i < length:
        if A[i] != elem:
            i += 1
        elif A[length - 1] == elem:
            length -= 1
        else:
            A[i] = A[length - 1]
            length -= 1
            i += 1
    return length
     