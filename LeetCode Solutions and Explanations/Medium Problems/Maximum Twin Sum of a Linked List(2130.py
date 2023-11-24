"""
Intuition
Since Linked Lists are directed we have to reverse the second half in order to calculate the twin sums.

To find the middle point we can use fast slow pointers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        def reverse_linked_list(head):
            prev = None
            current = head
            while current:

                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev

        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

    #    slow.next = None

        right_side_head = reverse_linked_list(slow)

        max_sum = 0

        current1 = head
        current2 = right_side_head

        while current1 and current2:
            max_sum = max(max_sum,current1.val+current2.val)
            current1 = current1.next
            current2 = current2.next

        return max_sum