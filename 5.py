# ������չ�����������Ӵ�
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start=end=0
        for i in range(len(s)):
            len1=self.centerexpand(s,i,i)
            len2=self.centerexpand(s,i,i+1)
            maxlen=max(len1,len2)
            if maxlen>end-start+1:
                start=i-(maxlen-1)//2
                end=i+maxlen//2
        return s[start:end+1]

    def centerexpand(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return r-l-1