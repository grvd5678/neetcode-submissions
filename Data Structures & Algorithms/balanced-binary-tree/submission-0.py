# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Our traditional helper function returns [is_balanced, height]
        def dfs(node):
            if not node:
                return [True, 0]
                
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Check if current node is balanced based on children's reports
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
                        
            # Return our status and our own height to the parent
            return [balanced, 1 + max(left[1], right[1])]
            
        return dfs(root)[0]