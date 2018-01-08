"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: The head of linked list.
    """

    def insertionSortList(self, head):
        dummy = ListNode(0)

        while head:
            temp = dummy
            next = head.next
            while temp.next and temp.next.val < head.val:
                temp = temp.next

            head.next = temp.next
            temp.next = head
            head = next

        return dummy.next

        # dummy = ListNode(0)

        # while head:
        #     temp = dummy
        #     next = head.next
        #     while temp.next and temp.next.val < head.val:
        #         temp = temp.next

        #     head.next = temp.next
        #     temp.next = head
        #     head = next

        # return dummy.next
