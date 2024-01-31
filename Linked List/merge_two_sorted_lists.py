from node import ListNode

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        
        list1_pointer = list1
        list2_pointer = list2
        head = None
        
        if list1_pointer.val < list2_pointer.val:
            head = list1_pointer
            list1_pointer = list1_pointer.next
        else:
            head = list2_pointer
            list2_pointer = list2_pointer.next

        curr = head

        while list2_pointer and list1_pointer:
            if list1_pointer.val < list2_pointer.val:
                curr.next = list1_pointer
                curr = curr.next
                list1_pointer = list1_pointer.next
            else:
                curr.next = list2_pointer
                curr = curr.next
                list2_pointer = list2_pointer.next

        if list1_pointer:
            curr.next = list1_pointer
        elif list2_pointer:
            curr.next = list2_pointer

        return head
    

if __name__ == "__main__":
    solution = Solution()
    # Create first sorted linked list: 1 -> 2 -> 4
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    # Create second sorted linked list: 1 -> 3 -> 4
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    # Merge the two sorted linked lists
    merged_head = solution.mergeTwoLists(l1, l2)

    # Print the merged linked list
    curr = merged_head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
                

