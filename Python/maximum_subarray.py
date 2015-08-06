class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        result = max(nums)
        if result <= 0 :
            return result
        s = 0
        for num in nums:
            s += num
            if s <= 0:
                s = 0
            elif s > result:
                result = s
        return result