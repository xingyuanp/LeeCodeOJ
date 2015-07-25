class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) - 2):
            low, high = i + 1, len(nums) - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s < target:
                    low += 1
                elif s > target:
                    high -= 1
                else:
                    return target
        return closest
