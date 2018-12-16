# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res=[]
        for i in lists:
            while i:
                res.append(i.val)
                i=i.next
        if res==[]:
            return []
        res.sort(reverse=True)
        l=ListNode(0)
        first=l
        while res:
            # the pop() function works from end, so the l should be reverse before.
            l.next=ListNode(res.pop())
            l=l.next
        # the first ListNode is inited as 0, so the return should be first.next.
        return first.next