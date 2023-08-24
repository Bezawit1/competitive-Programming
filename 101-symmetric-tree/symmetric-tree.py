# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return 0
        return self.checkSymmetry(root.left , root.right)
        
    def checkSymmetry (self , leftP , rightP):
        if leftP is None and rightP is None:
            return True
        if leftP is None or rightP is None:
            return False
        if leftP.val != rightP.val:
            return False
        outer = self.checkSymmetry(leftP.left, rightP.right)
        inner = self.checkSymmetry(leftP.right, rightP.left)
        return outer and inner