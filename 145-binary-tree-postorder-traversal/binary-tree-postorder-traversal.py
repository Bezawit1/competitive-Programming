# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return []
        res=[]
        leftP = self.postorderTraversal(root.left)
        rightP = self.postorderTraversal(root.right)
        res+=leftP
        res+=rightP
        res.append(root.val)
        return res