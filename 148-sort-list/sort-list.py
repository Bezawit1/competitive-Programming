# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
       
        values.sort()
        
        
        sorted_head = ListNode()
        current = sorted_head
        for val in values:
            current.next = ListNode(val)
            current = current.next
        
        return sorted_head.next

        