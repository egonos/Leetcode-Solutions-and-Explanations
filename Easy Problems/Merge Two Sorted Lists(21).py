"""
Intuition
The solution has couple key points:

Initialize an empty node to create a new sorted list.
Store the head of the new linked list (head).
Add the remainder part of the longer linked list.
Besides that the procedure is fairly simple. Add the smaller value of a linked list until reaching the end. To add the remainder part, we will use an additional statement.

Since the first node prev is only used for tracking, we need to it.

Time complexity: O(n)
Space complexity: O(1)

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        head = prev
        while list1 and list2:
            if list1.val<list2.val:
                prev.next = list1
                list1 = list1.next

            else:
                prev.next = list2
                list2 = list2.next

            prev = prev.next

        prev.next = list1 if list1 is not None else list2
        
        return head.next
            
        