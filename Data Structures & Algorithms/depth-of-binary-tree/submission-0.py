# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: an empty tree has a depth of 0!
        if not root:
            return 0
            
        # Traditionally recurse down both sides
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Add 1 for the current node, plus the deeper of the two branches
        return 1 + max(left_depth, right_depth)