# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        # Step 1: Detect cycle using Floyd's algorithm
        def get_meeting_point(head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None

        meet = get_meeting_point(head)
        if not meet:
            return None

        # Step 2: Find the start node of the cycle
        slow = head
        while slow != meet:
            slow = slow.next
            meet = meet.next

        return slow
