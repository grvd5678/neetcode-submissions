"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Map original nodes to their copies. 
        # Adding None: None saves us from annoying edge cases!
        oldToCopy = { None: None }
        
        # Step 1: Create all the clones
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
            
        # Step 2: Connect all the pointers
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
            
        # Return the head of the brand new cloned list!
        return oldToCopy[head]