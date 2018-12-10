class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=""
        if len(strs)==0:
            return ""
        # ������Ԫ�صĵ�ÿһ����Ӧ���ַ�ȡ�����γ�Ԫ��
        for each in zip(*strs):
            # �ж�Ԫ���е�Ԫ���Ƿ���ͬ
            if len(set(each))==1:
                res+=each[0]
            else:
                return res
        return res

s=Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))