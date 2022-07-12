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
        if not head:
            return None
        d ={}
        temp = head
        newHead = Node(0)
        newtemp = newHead
        while temp:
            newtemp.val = temp.val
            d[temp] = newtemp
            if temp.next:
                nextNode = Node(0)
                newtemp.next = nextNode
                newtemp = nextNode
            else: 
                newtemp.next = None
            temp = temp.next
        temp = head
        newtemp = newHead
        while temp:
            if temp.random:
                newtemp.random = d[temp.random]
            else:
                newtemp.random = None
            temp = temp.next
            newtemp = newtemp.next
        return newHead
            