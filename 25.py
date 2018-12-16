# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        current=head
        count=0
        while current and count!=k:
            current=current.next
            count+=1
        if count==k:
            current=self.reverseKGroup(current,k)
            # move each element from start of the segment to where it should be,
            # finally the current would be the start of each segment
            while count>0:
                temp=head.next
                head.next=current
                current=head
                head=temp
                count-=1
            head=current
        return head