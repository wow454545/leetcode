class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        ans = (re.match(p, s))
        if (ans == None):
            return False
        # group(0)��ʾƥ��������ַ���
        if (ans.group(0) != s):
            return False
        return True

s=Solution()
print (s.isMatch("ab", ".*c"))