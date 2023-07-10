class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        even=head.next
        odd= head
        even_node=even
        while odd.next and odd.next.next:
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=even_node
        return head
