class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        canJumpList = (len(nums) - 1) * [False] + [True]
        for start in reversed(range(len(nums) - 1)):
            step = 1
            while step <= nums[start]:
                nextStart = start + step
                if canJumpList[nextStart]:
                    canJumpList[start] = True
                    break
                elif nums[start] <= nums[nextStart] + step:
                    break
                else:
                    step += nums[nextStart] + 1
        return canJumpList[0]