# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        sorted_head = None

        while head:
            current = head
            head = head.next

            if not sorted_head or current.val < sorted_head.val:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and current.val > temp.next.val:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

        return sorted_head

  
        