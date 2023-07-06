class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode(None)
        current=dummy
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        if list1 is not None:
            current.next=list1
        if list2 is not None:
            current.next=list2
        return dummy.next
