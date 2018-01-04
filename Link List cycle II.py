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
    @return: The node where the cycle begins. if there is no cycle, return null
    """

    def detectCycle(self, head):
        if not head or not head.next:
            return None

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None
# 2(a + b) = a + b + c + b   -> a = c