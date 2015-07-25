class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        result = 0
        i = 1
        while n >= 5**i:
            result += n / (5**i)
            i += 1
        return result