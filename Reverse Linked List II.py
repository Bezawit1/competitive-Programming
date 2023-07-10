class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy=ListNode(None)
        dummy.next=head
        prev=dummy
        for _ in range(left-1):
            prev=prev.next

        start=prev
        end=prev.next
        for i in range(right-left):
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp
        return dummy.next
