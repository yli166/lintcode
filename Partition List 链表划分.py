#coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#链表 1->2->3->4->5 head是一个生成器 head.val = 1  head

class Solution(object):
    def partition(self, head, x):
        h1 = l1 = ListNode(0)   #设置h1 做为第一个指针的位置
        h2 = l2 = ListNode(0)

        while head:
            if head.val < x:       #head.val  = head[0]
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next

            head = head.next

        l2.next = None      #此时的指针位于 0->5->None 中的5 而h2 的指针位于 0-》5-》none 中的0
        l1.next = h2.next   #此时 l1的指针位于 1->2->3 中的3
                            #!!!!!!!!!!!!!!特别注意 l1.next = 某值时   h1 与 l1 还有关系  当 l1 = 某值时 h1 与 l1 切断关系

        return h1.next

head = [1,2,3,5,4]
x = 4

