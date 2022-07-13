# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        res = ListNode()
        temp3 = res
        carry = 0
        while temp1 or temp2:
            if temp1 and temp2:
                add = temp1.val + temp2.val + carry
                temp1 = temp1.next
                temp2 = temp2.next
            elif temp1:
                add = temp1.val +carry
                temp1 = temp1.next
            else:
                add= temp2.val +carry
                temp2 = temp2.next
            digit = add % 10
            carry = add // 10
            temp3.val = digit
            prev = temp3
            nextnode =ListNode()
            temp3.next = nextnode
            temp3 = nextnode
        if carry == 0:
            prev.next = None
        else:
            temp3.val = carry
            temp3.next = None
        
        return res
        