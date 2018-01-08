"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @param: k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        if not head:
            return None
        if k == 0:
            return head
        tmp = head
        count = 1
        while tmp.next:
            count += 1
            tmp = tmp.next
        tmp = dummy = ListNode(0)
        dummy.next = head
        num = k
        while num <= count:
            num += k
            pre = None
            cur = dummy
            curr = head
            for i in range(k -1):
                head = head.next
            next = head.next
            head.next = None
            while curr:
                node = curr
                curr = curr.next
                node.next = pre
                pre = node
            cur.next = pre
            for i in range(k -1):
                head = head.next
            head.next = next
            dummy = head
            head = head.next
        return tmp.next