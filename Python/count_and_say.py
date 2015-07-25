def countAndSay(n):
    if n == 1:
        return '1'
    
    previous = ''
    count = 0
    ans = ''
    for c in countAndSay(n-1):
        if c == previous:
            count += 1
        else:
            ans += str(count) + previous
            count = 1
            previous = c
    return ans[1:] + str(count) + previous