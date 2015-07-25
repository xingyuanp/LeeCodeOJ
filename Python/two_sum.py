class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        nums_set = set(nums)
        half_target = []
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums_set:
                if rem != nums[i]:
                    return [i + 1, nums.index(rem) + 1]
                else:
                    half_target.append(i + 1)
                    if len(half_target) == 2:
                        return half_target
                    
                