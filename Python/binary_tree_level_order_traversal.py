# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if root == None:
            return []
        leftPart = self.levelOrder(root.left)
        rightPart = self.levelOrder(root.right)
        n = min(len(leftPart), len(rightPart))
        
        # Use leftPart to holding the partial results
        for i in range(n):
                leftPart[i].extend(rightPart[i])
        if len(leftPart) < len(rightPart):
            leftPart.extend(rightPart[n:])
        
        # Build the final results by adding back root.val
        leftPart.insert(0, [root.val])
        return leftPart
