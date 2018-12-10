# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        tmp=ListNode(0)
        res=tmp
        flag=0
        while l1 or l2:
            tmp_sum=0
            if l1:
                tmp_sum=l1.val
                l1=l1.next
            if l2:
                tmp_sum+=l2.val
                l2=l2.next
            tmp_res=((tmp_sum+flag)%10)
            flag=((tmp_sum+flag)//10)
            res.next=ListNode(tmp_res)
            res=res.next
            if flag:
                res.next=ListNode(1)
        res=tmp.next
        del tmp
        return res