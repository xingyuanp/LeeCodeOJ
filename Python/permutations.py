class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        x = nums[-1]
        result = []
        for p in self.permute(nums[:-1]):
            for i in range(len(p) + 1):
                temp = p[:]
                temp.insert(i, x)
                result.append(temp)
        return result