class Solution(object):
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        prev = None
        node = head
        l1 = ListNode(0)
        while node:
            curr = node
            node = node.next
            curr.next = prev     # 改变了head的量 使head 变成了 n1 -> None
            prev = curr

        return prev, head



