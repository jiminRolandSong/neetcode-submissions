# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prevgroup = dummy


        while True:
            kth = prevgroup
            count = k
            while kth and count > 0:
                kth = kth.next
                count -= 1
                
            if not kth:
                break
            
            nextgroup = kth.next

            prev = kth.next
            current = prevgroup.next

            while current != nextgroup:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            
            nxt = prevgroup.next
            prevgroup.next = kth
            prevgroup = nxt
        
        return dummy.next



            

        