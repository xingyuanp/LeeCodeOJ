def longestCommonPrefix(strs):
    if strs == []:
        return ''
        
    minLen = len(strs[0])
    for string in strs:
        if len(string) < minLen:
            minLen = len(string)
    
    ans = ''
    for i in range(minLen):
        c = strs[0][i]
        for string in strs:
            if string[i] != c:
                return ans  
        ans += c
    return ans       
