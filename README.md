# leetcode
* AC all 945 problems before 1/3/2019 

> Now, I want to solve the problems as quickly as possible, so what I can do is forked the code and do my business.

* The class in python can be used and run directly like this:

`class Solution:  

    def isMatch(self, s, p):  
    
        """  
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        import re
        ans = (re.match(p, s))
        if (ans == None):
            return False
        # group(0)表示匹配的整个字符串
        if (ans.group(0) != s):
            return False
        return True
s=Solution()
print (s.isMatch("ab", ".*c"))`
