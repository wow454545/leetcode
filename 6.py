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
        # ��ǰ�������ȡ��ԭ�ַ����е�ֵ��
        # Ȼ�������������Ӧ���ڵ���
        for c in s:
            if row==0:
                step=1
            if row==numRows-1:
                step=-1
            zigzag[row]+=c
            row+=step
        # ��zigzag�б������е�Ԫ����''��������
        return ''.join(zigzag)