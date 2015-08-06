class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        def helper(x, n):
            if n == 0:
                return 1
            result = helper(x * x, n / 2)
            if n % 2 == 1:
                result *= x
            return result
        if n >= 0:
            return helper(x, n)
        else:
            return 1. / helper(x, -n)