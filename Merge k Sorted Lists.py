"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    # heap  O(NKlog(N))
    # def mergeKLists(self, lists):
    #     from heapq import heappush, heappop, heapreplace, heapify
    #     tmp = dummy = ListNode(0)
    #     h = [(n.val,n) for n in lists if n]
    #     heapify(h)
    #     while h:
    #         v,n = h[0]
    #         if n.next == None:
    #             heappop(h)
    #         else:
    #             heapreplace(h,(n.next.val,n.next))
    #         dummy.next = n
    #         dummy = dummy.next
    #     return tmp.next

    # merge 分治法
    def mergeKLists(self, lists):

        def merge(lst1, lst2):
            dummy = pt = ListNode(-1)
            while lst1 and lst2:
                if lst1.val < lst2.val:
                    pt.next = lst1
                    lst1 = lst1.next
                else:
                    pt.next = lst2
                    lst2 = lst2.next
                pt = pt.next

            pt.next = lst1 if not lst2 else lst2
            return dummy.next

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]
        mid = len(lists) / 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return merge(left, right)