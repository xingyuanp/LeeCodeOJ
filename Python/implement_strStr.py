def strStr(haystack, needle):
    def match(s, needle):
        if len(s) < len(needle):
            return False
        for i in range(len(needle)):
            if s[i] != needle[i]:
                return False
        return True
    
    if needle == '':
        return 0    
    for i in range(len(haystack)):
        if match(haystack[i:], needle):
            return i
    return -1
   
    
     
       
def strStr2(haystack, needle):
    if needle == '':
        return 0
    for i in range(len(haystack)):
        for j in range(len(needle)):
            if i + j >= len(haystack):
                return -1
            if haystack[i+j] != needle[j]:
                break
        else:
            return i
    return -1