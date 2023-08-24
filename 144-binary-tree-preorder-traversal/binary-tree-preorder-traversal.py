# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        res=[]
        res.append(root.val)
        leftP = self.preorderTraversal(root.left)
       
        rightP = self.preorderTraversal(root.right)
        res +=leftP
        res += rightP
        return res
    
       