# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        levelT  = []
        
        if root is None:
            return levelT
        arr = [root]
        while arr:
            nodes = []

            for _ in range(len(arr)):
                current = arr.pop(0)
                nodes.append(current.val)
                if current.left:
                    arr.append(current.left)
                if current.right:
                    arr.append(current.right)
            levelT.append(nodes)
        return levelT
       
        
       
            

        