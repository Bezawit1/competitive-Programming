# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    total_sum = 0
    def sumEvenGrandparent(self, root):
        # check if the current node is even if even add the next next value to the sum
        # do the same for each node 
        
        if not root :
            return 0
        if root.val % 2 == 0:
            if root.right and root.right.right:
                self.total_sum+=root.right.right.val
            if root.right and root.right.left:
                self.total_sum+=root.right.left.val
            if root.left and root.left.right:
                self.total_sum+=root.left.right.val
            if root.left and root.left.left:
                self.total_sum+=root.left.left.val
        self.sumEvenGrandparent(root.right)
        self.sumEvenGrandparent(root.left)
        return self.total_sum


        
       
        