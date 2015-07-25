import sys

def atoi(str):
    maxOver10 = sys.maxint / 10
    maxRem10 = sys.maxint % 10
    
    str = str.strip()
    if str == '':
        return 0
    
    sign = 1
    if str[0] == '-':
        sign = -1
    if str[0] in '+-':
        str = str[1:]
    
    ans = 0
    for c in str:
        if c.isdigit():
            i = int(c)
            if (ans == maxOver10 and i > maxRem10) or (ans > maxOver10):
                if sign == 1:
                    return sys.maxint
                else:
                    return -(sys.maxint + 1)
            ans = 10 * ans + i  
        else:
            break         
    return sign * ans               
