# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # An empty subRoot is technically a subtree of anything!
        if not subRoot:
            return True
        # If we run out of main tree, we didn't find it
        if not root:
            return False
            
        # Check if the tree starting at this exact node is a perfect match
        if self.isSameTree(root, subRoot):
            return True
            
        # Otherwise, traditionally recurse down to check the left and right sides
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
                
    # Our iconic helper from the last problem!
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))