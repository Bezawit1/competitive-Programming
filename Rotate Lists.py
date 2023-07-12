
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
             return head
        
        length = 1
        last = head
        while last.next:
            length += 1
            last = last.next

        
        k = k % length
        if k == 0:
            return head

        
        new_head_pos = length - k
        curr = head
        for _ in range(new_head_pos - 1):
            curr = curr.next

        
        new_head = curr.next
        curr.next = None
        last.next = head

        return new_head
