from node import ListNode

class Solution(object):
    def reverseList(self, head):
        curr = head
        next = None
        prev = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev