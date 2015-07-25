class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        memory = {}
        def helper(n_left, n_right):
            if (n_left, n_right) in memory:
                return memory[(n_left, n_right)]
            if n_left == 0:
                return [n_right * ')']
            if n_left > n_right:
                return []     
            part1 = ['(' + x for x in helper(n_left - 1, n_right)]
            part2 = [')' + x for x in helper(n_left, n_right - 1)]
            memory[(n_left, n_right)] = part1 + part2
            return memory[(n_left, n_right)]
        return helper(n, n)