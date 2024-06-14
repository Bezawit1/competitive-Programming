# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        def balanceTree(values):
            if not values:
                return None
            mid = len(values) // 2
            root = TreeNode(values[mid])
            root.left = balanceTree(values[:mid])
            root.right = balanceTree(values[mid+1:])
            return root
        
        sorted_values = inorder(root)
        return balanceTree(sorted_values)