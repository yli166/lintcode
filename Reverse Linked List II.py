"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: ListNode head is the head of the linked list
    @param: m: An integer
    @param: n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        head1 = head
        tmp = dummy = ListNode(0)
        dummy.next = head
        pre = None
        count = 1
        while head.next:
            count += 1
            if m <= count <= n:
                cur = head.next.next
                head.next.next = pre
                pre = head.next
                head.next = cur
                continue
            head = head.next
        for i in range(m - 1):
            dummy = dummy.next
        cur = dummy.next
        dummy.next = pre
        while pre.next:
            pre = pre.next
        pre.next = cur
        return tmp.next