class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        # Traditional Pre-order DFS
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0  # A global pointer to keep track of where we are in the list
        
        # Traditional Recursive Builder
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
                
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            
            # The order must perfectly match our serialization (Left, then Right)
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()