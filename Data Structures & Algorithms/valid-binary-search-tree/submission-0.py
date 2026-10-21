# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Our trusty, traditional helper function!
        def valid(node, left_boundary, right_boundary):
            # Base case: an empty node is perfectly valid!
            if not node:
                return True
                
            # If the current node breaks the boundary rules, it's invalid!
            if not (left_boundary < node.val < right_boundary):
                return False
                
            # Recurse left (update max ceiling) AND recurse right (update min floor)
            return (valid(node.left, left_boundary, node.val) and 
                    valid(node.right, node.val, right_boundary))
            
        # Start at the root with infinite boundaries!
        return valid(root, float("-inf"), float("inf"))