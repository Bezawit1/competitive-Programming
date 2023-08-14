# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == 1
        left_result = self.evaluateTree(root.left)
        right_result = self.evaluateTree(root.right)
        
        if root.val == 2:
            return left_result or right_result
        if root.val == 3:
            return left_result and right_result