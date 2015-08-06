class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        def helper(m, n, d={}):
            if m > n:
                m, n = n, m
            if m == 1:
                return 1
            try:
                return d[(m, n)]
            except KeyError:
                result = helper(m - 1, n, d) + helper(m, n - 1, d)
                d[(m, n)] = result
                return result
        return helper(m, n)