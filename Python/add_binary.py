def addBinary(a, b):
    def binary_to_decimal(s):
        ans = 0
        power = len(s) - 1
        for c in s:
            ans += int(c) * 2**power
            power -= 1
        return ans
    
    def decimal_to_binary(n):
        if n == 0:
            return '0'
        ans = ''
        while n > 0:
            ans = str(n % 2) + ans
            n /= 2
        return ans
        
    sum = binary_to_decimal(a) + binary_to_decimal(b)
    return decimal_to_binary(sum)

        
def addBinary2(a, b):
    if len(a) < len(b):
        a, b = b, a
    b = (len(a) - len(b)) * '0' + b
   
    ans = ''
    carry = '0'
    for m, n in reversed(zip(a, b)):
        if m != n and carry == '0':
            ans = '1' + ans
        elif m != n and carry == '1':
            ans = '0' + ans
        else:
            ans = carry + ans
            carry = m
    if carry == '1':
        ans = '1' + ans
    return ans