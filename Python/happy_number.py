class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        explored = set()
        while n != 1 and n not in explored:
            explored.add(n)
            s = 0
            while n > 0:
                s += (n % 10)**2
                n /= 10
            n = s
        return n == 1
