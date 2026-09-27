# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        
        while curr:
            # If both p and q are greater, LCA must be in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both p and q are lesser, LCA must be in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # We found the split point (or one of them is the current node)!
            else:
                return curr