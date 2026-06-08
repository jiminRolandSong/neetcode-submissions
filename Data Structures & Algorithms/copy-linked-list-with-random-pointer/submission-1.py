"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2copy = {None: None}

        old = head
        while old:
            copy = Node(old.val)
            old2copy[old] = copy
            old = old.next
        
        old = head
        while old:
            copy = old2copy[old]
            copy.next = old2copy[old.next]
            copy.random = old2copy[old.random]
            old = old.next
        
        return old2copy[head]
        