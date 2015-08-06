class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        from math import factorial as f
        nums = range(1, n + 1)
        result = ''
        for i in range(n):
            q, r = k / f(n - 1 - i), k % f(n - 1 - i)
            if r > 0:
                q += 1
            result += str(nums[q - 1])
            nums.remove(nums[q - 1])
            k = r
        return result