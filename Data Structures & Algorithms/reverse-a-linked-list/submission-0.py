# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next   # Save the next node
            curr.next = prev  # Reverse the pointer
            prev = curr       # Shift prev forward
            curr = nxt        # Shift curr forward
            
        return prev