class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=""
        if len(strs)==0:
            return ""
        # 将所有元素的第每一个对应的字符取出来形成元组
        for each in zip(*strs):
            # 判断元组中的元素是否相同
            if len(set(each))==1:
                res+=each[0]
            else:
                return res
        return res

s=Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))