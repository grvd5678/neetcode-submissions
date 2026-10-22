# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Start with negative infinity just in case all nodes are negative!
        self.max_sum = float('-inf')
        
        # Our trusty, traditional DFS helper
        def dfs(node):
            if not node:
                return 0
                
            # Ask the left and right children for their max paths.
            # If they are negative, we literally just ignore them and use 0!
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            # The maximum path if it peaks at this specific node (the V-shape)
            current_path_sum = node.val + left_max + right_max
            
            # Update our global tally if we found a new winner
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # We can only return ONE straight path up to the parent!
            return node.val + max(left_max, right_max)
            
        dfs(root)
        return self.max_sum