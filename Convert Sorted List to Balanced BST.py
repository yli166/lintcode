"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, head):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head.next.next
        while fast and fast.next:  # 先借一位 方便将left结扎
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next
        right = tmp.next
        slow.next = None
        left = head
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root