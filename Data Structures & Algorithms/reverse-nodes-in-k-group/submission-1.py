# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            kth = prev_group # 0 -> 3
            count = 0
            while kth and count < k:
                kth = kth.next
                count += 1

            if not kth:
                break

            next_group = kth.next #4

            current = prev_group.next
            prev = kth.next 

            while current != next_group:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            new_start = prev_group.next # 1
            prev_group.next = kth #3
            prev_group = new_start
        
        return dummy.next
        