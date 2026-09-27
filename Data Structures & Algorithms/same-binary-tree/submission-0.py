# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are empty, they perfectly match!
        if not p and not q:
            return True
            
        # If only one is empty, or the values are different, it's a mismatch!
        if not p or not q or p.val != q.val:
            return False
            
        # Traditionally recurse down the left and right sides simultaneously
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))