# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if root.left == root.right == None:
            return root.val == sum
        return (self.hasPathSum(root.left, sum - root.val) 
                or self.hasPathSum(root.right, sum - root.val))