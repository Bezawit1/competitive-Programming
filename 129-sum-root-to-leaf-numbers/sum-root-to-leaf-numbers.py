# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        self.sum = 0
        def dfs (node , curr_sum ):
            if not node:
                    return False
            curr_sum = curr_sum * 10 + node.val
            left_node = dfs(node.left , curr_sum)
            right_node = dfs(node.right , curr_sum)
            if not left_node and not right_node:
                self.sum +=curr_sum
            return True
        dfs(root , 0)
        return self.sum
            