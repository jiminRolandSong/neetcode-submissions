# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy

        for i in range(left - 1):
            prev = prev.next
        
        sub_head = prev.next
        sub_tail = sub_head

        for i in range(right-left):
            sub_tail = sub_tail.next

        sub_next = sub_tail.next
        sub_tail.next = None

        current = sub_head
        new_prev = None

        while current:
            nxt = current.next
            current.next = new_prev
            new_prev = current
            current = nxt
        
        prev.next = new_prev
        sub_head.next = sub_next

        return dummy.next
        

        
        
            

        