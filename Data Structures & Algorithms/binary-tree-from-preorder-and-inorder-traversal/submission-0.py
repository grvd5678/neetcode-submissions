
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map inorder values to their indices for instant O(1) lookups!
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        
        # Our trusty, traditional DFS helper!
        def build(left, right):
            # Base case: if boundaries cross, there's no subtree here
            if left > right:
                return None
                
            # The current root is always the next item in preorder
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Find exactly where this root splits the inorder array
            mid = inorder_map[root_val]
            
            # Recursively build the left and right sides!
            # (Left must be built first because preorder is Root -> Left -> Right)
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
            
        # Start the build using the entire inorder array boundaries
        return build(0, len(inorder) - 1)