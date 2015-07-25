class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        result = ''
        
        for c in range(len(s)):
            i = j = c
            while 0 <= i and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            if len(result) < j - i - 1:
                result = s[i+1:j]
                
        for c in range(len(s)):
            i, j = c, c + 1
            while 0 <= i and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            if len(result) < j - i - 1:
                result = s[i+1:j]
            
        return result