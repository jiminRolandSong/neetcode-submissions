# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(l1, l2):
            dummy = ListNode(0)
            node = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            node.next = l1 or l2

            return dummy.next
        
        if len(lists) < 1:
            return None
        
        final_merge = lists[0]
        for i in range(1, len(lists)):
            final_merge = merge(final_merge, lists[i])
        
        return final_merge

        