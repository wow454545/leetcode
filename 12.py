class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        numerals=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        alist=''
        for i in range(0,len(values)):
            while num>=values[i]:
                num-=values[i]
                alist+=numerals[i]
        return alist