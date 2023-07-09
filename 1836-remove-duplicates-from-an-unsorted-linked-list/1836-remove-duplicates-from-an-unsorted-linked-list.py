# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        d = defaultdict(int)
        temp = head
        while temp:
            d[temp.val] += 1
            temp = temp.next
        temp = head
        prev = None

        while temp:
          
            if prev and d[temp.val] > 1:

                prev.next = temp.next
            elif not prev and d[temp.val] > 1:
                head = temp.next
            else:
                prev = temp
            temp = temp.next


        return head