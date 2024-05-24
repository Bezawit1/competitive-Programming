# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

     
        vertical_levels = defaultdict(list)
        
    
        def dfs(node, col, row):
            if node is None:
                return
            vertical_levels[col].append((row, node.val))
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)
        
       
        dfs(root, 0, 0)
        
       
        sorted_vertical_levels = []
        for col in sorted(vertical_levels.keys()):
            sorted_vertical_levels.append([val for row, val in sorted(vertical_levels[col])])
        
        return sorted_vertical_levels