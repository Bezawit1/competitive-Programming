# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        res = []
        if not head:
            return None
        current = head
        while current and current.next:
            res.append(current.val)
            current = current.next
        res.append(current.val)
    
        stringVal = "".join(str(x) for x in res)
        num_val = int(stringVal,2)
        
        return num_val
        