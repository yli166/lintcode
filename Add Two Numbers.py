class Solution:
    """
    @param: l1: the first list
    @param: l2: the second list
    @return: the sum list of l1 and l2
    """

    def addLists(self, l1, l2):
        tmp = dummy = ListNode(0)
        count = 0

        while True:

            if l1:
                count += l1.val
                l1 = l1.next
            if l2:
                count += l2.val
                l2 = l2.next
            int = count % 10
            count = count / 10
            dummy.val = int
            if l1 != None or l2 != None:
                dummy.next = ListNode(0)
                dummy = dummy.next
            else:
                break

        return tmp.next