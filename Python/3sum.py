class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        solution_set = set()
        for i in range(len(nums)):
            low, high = i + 1, len(nums) - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if s == 0:
                    triplet = (nums[i], nums[low], nums[high])
                    if triplet not in solution_set:
                        solution_set.add(triplet)
                    low += 1
                    high -= 1
                elif s < 0:
                    low += 1
                else:
                    high -= 1
        return list(solution_set)