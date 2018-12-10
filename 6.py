class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        zigzag=['' for i in range(numRows)]
        row=0
        step=1
        # 从前往后逐个取出原字符串中的值，
        # 然后再逐个插入其应该在的行
        for c in s:
            if row==0:
                step=1
            if row==numRows-1:
                step=-1
            zigzag[row]+=c
            row+=step
        # 将zigzag列表中所有的元素用''连接起来
        return ''.join(zigzag)