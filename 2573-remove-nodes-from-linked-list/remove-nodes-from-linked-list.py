# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node):
            prev = None
            curr = node
            while curr:
                forw = curr.next
                curr.next = prev
                prev = curr
                curr = forw
            return prev
        
        head = reverse(head)

        max_val = head.val
        curr = head
        
        while curr and curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.val
        
        head = reverse(head)

        return head
