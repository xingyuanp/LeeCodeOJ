def isPalindrome(x):
    if x < 0:
        return False
    maxint = 2147483647
    temp = x
    r = 0
    while temp > 0:
        if r > maxint / 10:
            return False
        r = 10 * r + temp % 10 
        temp /= 10
    return r == x