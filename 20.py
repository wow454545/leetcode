class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a={')':'(',']':'[','}':'{'}
        l=[None] # now, the length of l is one.
        for i in s:
            # the comment fails the running
            # l[-1]ȡ�������һ��Ԫ��
            if i in a and a[i]==l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l)==1

s=Solution()
print(s.isValid('(){}[]'))