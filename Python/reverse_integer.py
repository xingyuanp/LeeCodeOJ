def reverse(x):
    negative = (x < 0)
    x = abs(x)
    
    result = 0
    while x > 0:
        current = x % 10
        if result > 214748364:
            return 0
        result = 10 * result + current
        x = x / 10
    
    if negative:
        result = - result       
    return result
    