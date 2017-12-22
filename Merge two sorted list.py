class Solution:
    """
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """

    def mergeTwoLists(self, l1, l2):
        # write your code here

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        tmp = dummy = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next

        if l1:
            dummy.next = l1
        else:
            dummy.next = l2

        return tmp.next