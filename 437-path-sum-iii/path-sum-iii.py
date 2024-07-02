# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        path_sum = defaultdict(int)
        path_sum[0] = 1
        
        def dfs(root, curr_sum):
            count = 0
            if root:
                curr_sum += root.val
                count = path_sum[curr_sum - targetSum]
                path_sum[curr_sum] += 1
                count += dfs(root.left, curr_sum) + dfs(root.right, curr_sum)
                path_sum[curr_sum] -= 1
            return count
        return dfs(root, 0)
        
     
        