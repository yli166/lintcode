"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        # len(A) - len(B)
        # curA = headA
        # curB = headB
        # lenA,lenB = 0,0

        # while curA:
        #     lenA += 1
        #     curA = curA.next
        # while curB:
        #     lenB += 1
        #     curB = curB.next
        # curA = headA
        # curB = headB
        # if lenA > lenB:
        #     for i in range(lenA-lenB):
        #         curA = curA.next
        # elif lenB > lenA:
        #     for i in range(lenB-lenA):
        #         curB = curB.next
        # while curB != curA:
        #     curB = curB.next
        #     curA = curA.next
        # return curA


        # loop
        if not headA or not headB:
            return None

        tmp = headA
        while tmp.next:
            tmp = tmp.next
        mark = tmp
        mark.next = headA
        slow = headB
        fast = headB

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast == slow:
            slow = headB
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None