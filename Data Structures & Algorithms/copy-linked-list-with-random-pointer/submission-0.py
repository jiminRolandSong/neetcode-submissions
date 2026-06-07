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

        old2copy = {None:None}

        current = head

        while current:
            copy = Node(current.val)
            old2copy[current] = copy
            current = current.next
        
        current = head

        while current:
            copy = old2copy[current]
            copy.next = old2copy[current.next]
            copy.random = old2copy[current.random]
            current = current.next
        
        return old2copy[head]



        