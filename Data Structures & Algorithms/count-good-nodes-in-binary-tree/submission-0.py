# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Our trusty, traditional DFS helper!
        def dfs(node, max_val):
            # Base case: empty node means 0 good nodes
            if not node:
                return 0
                
            # Is this current node a "good" node?
            res = 1 if node.val >= max_val else 0
            
            # Update the max value for the children to see
            new_max = max(max_val, node.val)
            
            # Recursively check the left and right branches
            res += dfs(node.left, new_max)
            res += dfs(node.right, new_max)
            
            return res
            
        # Start the DFS at the root, with the root's own value as the initial max
        return dfs(root, root.val)