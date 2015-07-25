# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        result = []
        if root == None:
            return result
            
        leftPart = self.levelOrderBottom(root.left)
        rightPart = self.levelOrderBottom(root.right)
        n_left, n_right = len(leftPart), len(rightPart)
        n = min(n_left, n_right)
        
        for i in range(-n, 0):
            leftPart[i].extend(rightPart[i])
        if n_left < n_right:
            result.extend(rightPart[:n_right - n])
        result.extend(leftPart)
        result.extend([[root.val]])
        
        return result