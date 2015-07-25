class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d = {i: letters[i] for i in range(26)}
        result = ''
        while n > 0:
            result = d[(n - 1) % 26] + result
            n = (n - 1) / 26
        return result