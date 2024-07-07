# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        visited = []
        queue = deque([root])
        if not root:
            return visited
       
        while queue:
            nodes = []
            for _ in range(len(queue)):
                current = queue.popleft()
                nodes.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                
            visited.append(nodes)
        return visited

            
            
        