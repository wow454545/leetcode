class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        sum=0
        # 从个位数开始计算
        s=s[::-1]
        last=None
        # x为当前位，last为上一位
        for x in s:
            if last and numerals[x]<last:
                sum-=2*numerals[x]
            sum+=numerals[x]
            last=numerals[x]
        return sum

s=Solution()
print(s.romanToInt("IV"))