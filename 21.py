# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        # 这里用head去添加next节点，用first保存第一个节点
        first=head
        while l1!=None and l2!=None:
            if l1.val>l2.val:
                head.next=l2
                l2=l2.next
            else:
                head.next=l1
                l1=l1.next
            head=head.next
        if l1==None:
            head.next=l2
        elif l2==None:
            head.next=l1
        return first.next