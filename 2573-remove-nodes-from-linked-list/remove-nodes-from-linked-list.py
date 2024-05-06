class Solution(object):
    def removeNodes(self, head):
        stack = []
        current = head
        
        while current:
            next_node = current.next
            
            while stack and stack[-1].val < current.val:
                stack.pop()
            
            if stack:
                stack[-1].next = current
            
            stack.append(current)
            
            current = next_node
        
        if stack:
            stack[-1].next = None
        
        return stack[0] if stack else None
