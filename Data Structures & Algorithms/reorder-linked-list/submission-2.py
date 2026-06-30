# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        current = second
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        first = head
        second = prev

        while first and second:
            temp_one = first.next
            temp_two = second.next

            first.next = second
            second.next = temp_one

            first = temp_one
            second = temp_two

        

        

        