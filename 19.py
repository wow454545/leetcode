# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre=head
        end=head
        # the “_” means just read but do not use the iterator from 0,1,...,n-1
        for _ in range(n):
            end=end.next
        if end is None:
            return head.next
        # 以上操作以后，有两个作用，一是如果去掉的是第一个节点，直接返回head.next;
        # 二是确定了pre和end的距离为n，所以当end为最后一个节点时，pre.next正是需要删除的节点
        while end.next is not None:
            pre=pre.next
            end=end.next
        # 在pre中就修改了head的结构
        pre.next=pre.next.next
        return head

