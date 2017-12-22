class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        if n == 0:
            return head

        count = 0

        node = head

        while node:
            count += 1
            node = node.next

        l1 = ListNode(0)

        l1.next = head

        f1 = l1  # 他们此时都是0 游标都在0上

        for each in range(count - n):
            l1 = l1.next

        l1.next = l1.next.next

        return f1.next