class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        :这里没有考虑前面字符为字母的情况，就AC了
        """
        # 去除字符串首位的特定字符
        s=str.strip()
        symbol,ptr,res=1,0,0
        if len(s)==0:
            return 0
        if s[0]=='-':
            symbol=-1
            s=s[1:]
        elif s[0]=='+':
            s=s[1:]
        if len(s)==0:
            return 0
        while s[ptr].isnumeric():
            res=res*10+int(s[ptr])
            ptr+=1
            if ptr>=len(s):
                break
        res=res*symbol
        if res>2147483647:
            res=2147483647
        elif res<-2147483648:
            res=-2147483648
        return res

