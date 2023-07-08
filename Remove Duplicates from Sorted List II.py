class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        prev = ListNode(None)
        prev.next = head
        head = prev

        while current and current.next:
            if current.val == current.next.val:
                duplicate_value = current.val
                while current and current.val == duplicate_value:
                    current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next

        if prev.next:
            prev.next = current

        return head.next
