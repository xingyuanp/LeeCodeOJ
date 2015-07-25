def removeElement(A, elem):
    """Given an array and a value, remove all instances of that value in place
    and return the new length. The order of elements can be changed. It doesn't
    matter what you leave beyond the new length.
    
    A: a list of integers
    elem: an integer, value need to be removed
    return an integer"""
    
    while True:
        try:
            A.remove(elem)
        except ValueError:
            break
    return len(A)
            
            