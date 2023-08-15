# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        res=[]
        left_path = self.inorderTraversal(root.left)
        res =  left_path + [root.val]
        right_path = self.inorderTraversal(root.right)
        res += right_path
        return res
    
        