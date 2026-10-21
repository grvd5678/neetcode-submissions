import collections
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
            
        # Initialize our traditional queue with the root
        q = collections.deque([root])
        
        while q:
            level_size = len(q)
            
            # Process every node on this level
            for i in range(level_size):
                node = q.popleft()
                
                # If this is the absolute last node in the level, we can see it!
                if i == level_size - 1:
                    res.append(node.val)
                    
                # Queue up the children for the next level (left then right)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return res