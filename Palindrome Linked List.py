class Solution(object):
    def isPalindrome(self, head):
        arr=[]

        while head!=None:
            arr.append(head.val)
            head=head.next
        return arr==arr[::-1]
