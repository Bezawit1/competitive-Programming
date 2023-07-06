class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast=head
        slow=head
        prev=None
        current=head
        for _ in range(n):
            if fast is None:
               return head  
            fast = fast.next
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next
        if prev is None:
            head = head.next
        else:
            prev.next = slow.next
        return head
