class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            head = head
        else:

            slow = fast = head  # two parts
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            head2 = slow.next
            slow.next = None

            dummy = ListNode(0)  # reverse 2nd part
            dummy.next = head2
            p = head2.next
            head2.next = None     #设置中间值   #######################head2 = ListNode(head.val) head2.next = head.next ############################
            while p:
                tmp = p
                p = p.next
                tmp.next = dummy.next
                dummy.next = tmp
            head2 = dummy.next

            p1 = head  # rejoin 2 parts together
            p2 = head2
            while p2:
                t1 = p1.next
                p1.next = p2
                t2 = p2.next
                p2.next = t1
                p1 = t1
                p2 = t2