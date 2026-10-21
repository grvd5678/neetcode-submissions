import collections
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
            
        # Initialize our trusty queue with the root
        q = collections.deque([root])
        
        while q:
            level_size = len(q)
            level_vals = []
            
            # Process every single node currently on this level
            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)
                
                # Queue up the children for the next level!
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            # Add this completed level to our final result
            res.append(level_vals)
            
        return res