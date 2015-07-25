class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        d = []
        for i in range(len(nums)):
            if i == 0:
                d.append(nums[0])
            elif i == 1:
                d.append(max(nums[0], nums[1]))
            else:
                d.append(max(d[i - 2] + nums[i], d[i - 1]))
        return d[-1]
        