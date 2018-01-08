"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: the List
    @param: k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        if not head:
            return None
        if k == 0:
            return head
        head1 = head
        count = 1
        while head.next:
            count += 1
            head = head.next
        head.next = head1
        m = count - k % count
        for i in range(m):
            head = head.next
        begin = head.next
        head.next = None
        return begin