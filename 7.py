class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # x[::-1]��ʾ�Ӻ���ǰȡֵ������Ϊ1
        x=int(str(x)[::-1]) if x>=0 else -int(str(-x)[::-1])
        return x if x<2147483648 and x>=-2147483648 else 0
