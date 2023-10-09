# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
            def helper(lists):
                res = []
                for i in lists:
                    while i:
                        res.append(i.val)
                        i = i.next
                return res

            def linked_list(nums):
                dummy = ListNode()
                current = dummy
                for num in nums:
                    current.next = ListNode(num)
                    current = current.next
                return dummy.next

            flattened_list = helper(lists)
            flattened_list.sort()

            sorted_list = linked_list(flattened_list)

            return sorted_list
        
        