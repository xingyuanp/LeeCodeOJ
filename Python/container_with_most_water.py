class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):            
        i, j = 0, len(height) - 1
        area = 0
        while i < j:
            area = max(area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area