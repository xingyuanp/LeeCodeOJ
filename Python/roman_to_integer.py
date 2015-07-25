def romanToInt(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    i = 0
    while i < len(s) - 1:
        currentChar, nextChar = s[i], s[i+1]
        if d[currentChar] < d[nextChar]:
            ans -= d[currentChar]
        else:
            ans += d[currentChar]        
        i += 1
    ans += d[s[-1]]
    return ans