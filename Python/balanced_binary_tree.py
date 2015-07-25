# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        def getDepth(node):
            if node == None:
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))
            
        if root == None:
            return True
        return (self.isBalanced(root.left) and self.isBalanced(root.right)
                and abs(getDepth(root.left) - getDepth(root.right)) <=1)