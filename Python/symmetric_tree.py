# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        def isSymmetric_twoTrees(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None and root2 != None:
                return False
            if root1 != None and root2 == None:
                return False
            if root1.val != root2.val:
                return False
            return (isSymmetric_twoTrees(root1.left, root2.right) 
                    and isSymmetric_twoTrees(root1.right, root2.left))
        
        if root == None:
            return True
        return isSymmetric_twoTrees(root.left, root.right)