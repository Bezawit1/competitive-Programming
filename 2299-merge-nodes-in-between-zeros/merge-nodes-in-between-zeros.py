class Solution(object):
    def mergeNodes(self, head):
        if not head:
            return None
        
        current = head
        pointer = head.next
        running_sum = 0
        while pointer:
            if pointer.val == 0:
                current = current.next
                current.val=running_sum
                running_sum=0
            else:
                running_sum+=pointer.val
            pointer = pointer.next
        current.next=None
        return head.next
