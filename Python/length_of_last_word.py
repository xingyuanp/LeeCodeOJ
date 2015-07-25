def lengthOfLastWord(s):
    i = 0
    for i in range(len(s)):
        if s[-1-i] != ' ':
            break
    s = s[:len(s)-i]
    for i in range(len(s)):
        if s[-1-i] == ' ':
            return i
    return len(s)
