# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def deleteNode(self, root, key):
        if root is None:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # If the node is with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # If the node has two children,
            # place the inorder successor in position of the node to be deleted
            temp = self.minValueNode(root.right)
            root.val = temp.val
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)
            
        return root
