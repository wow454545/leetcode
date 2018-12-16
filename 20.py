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
            # l[-1]取的是最后一个元素
            if i in a and a[i]==l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l)==1

s=Solution()
print(s.isValid('(){}[]'))