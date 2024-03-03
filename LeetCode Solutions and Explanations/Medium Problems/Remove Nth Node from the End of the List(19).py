# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #single node case
        if not head.next:
            return
        
        #count the nodes
        current = head
        nodes = 1
        while current.next:
            current = current.next
            nodes +=1

        #find the previous node of removal node
        target = nodes - n - 1

        #start case
        if n == nodes:
            return head.next

        current = head
        for _ in range(target):
            current = current.next
        #middle values
        try:
            current.next = current.next.next
        #last value
        except:
            current.next = None

        return head
        