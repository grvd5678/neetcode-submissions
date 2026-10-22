# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while stack or curr:
            # 1. Dive as far left as possible to find the smallest elements
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # 2. Pop the smallest available node and process it
            curr = stack.pop()
            k -= 1
            
            # 3. If we've popped exactly k times, we found our answer!
            if k == 0:
                return curr.val
                
            # 4. Move to the right subtree to continue the in-order sequence
            curr = curr.right