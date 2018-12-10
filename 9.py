class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        l=len(s)
        if l in [0,1]:
            return True
        if x<0:
            return False
        for i in range(l//2):
            if s[i]!=s[l-i-1]:
                return False
        return True