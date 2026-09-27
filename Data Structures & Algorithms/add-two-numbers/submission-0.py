# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # Grab values if the nodes exist, otherwise use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Classic addition!
            total = val1 + val2 + carry
            carry = total // 10
            
            # Add the ones-place digit to our new list
            curr.next = ListNode(total % 10)
            
            # Shift all our pointers forward
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next