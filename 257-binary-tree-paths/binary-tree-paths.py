# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        res = []
        if not root:
            return None
        def backtrack(candidate ,path):
            
            if candidate.right == None and candidate.left == None:
                res.append("->".join(path))
                return
            if(candidate.right):
            
                path.append(str(candidate.right.val))
                backtrack(candidate.right , path)
                path.pop()
            if(candidate.left):
                path.append(str(candidate.left.val))
                backtrack(candidate.left , path)
                path.pop()

        backtrack(root , [str(root.val)])
        return res
        
            