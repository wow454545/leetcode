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
        # the ��_�� means just read but do not use the iterator from 0,1,...,n-1
        for _ in range(n):
            end=end.next
        if end is None:
            return head.next
        # ���ϲ����Ժ����������ã�һ�����ȥ�����ǵ�һ���ڵ㣬ֱ�ӷ���head.next;
        # ����ȷ����pre��end�ľ���Ϊn�����Ե�endΪ���һ���ڵ�ʱ��pre.next������Ҫɾ���Ľڵ�
        while end.next is not None:
            pre=pre.next
            end=end.next
        # ��pre�о��޸���head�Ľṹ
        pre.next=pre.next.next
        return head

