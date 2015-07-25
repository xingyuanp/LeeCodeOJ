class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d = {letters[i]: i + 1 for i in range(26)}
        result = 0
        for letter in s:
            result = result * 26 + d[letter]
        return result