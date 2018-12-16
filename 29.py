class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag=-1 if (dividend<0 and divisor>0) or (dividend>0 and divisor<0) else 1
        dividend, divisor=abs(dividend),abs(divisor)
        if dividend<divisor:
            return 0
        if dividend==divisor:
            return flag
        if divisor==1:
            return flag*dividend if flag*dividend<2**31 else 2**31-1
        # the range(start,stop,step) works from start to stop-1, so here will be dividend+1 instand.
        return flag*len(range(divisor,dividend+1,divisor))
s=Solution()
print(s.divide(9,3))
