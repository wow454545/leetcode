class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        Num=0
        for i in range(0,len(s)):
            ns=''
            # 从j开始往后取符合条件的最大字符串
            for j in s[i:]:
                if j not in ns:
                    ns=ns+j
                    num=len(ns)
                else:
                    break

            if num>Num:
                Num=num

        return Num