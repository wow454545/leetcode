# leetcode
* AC all 945 problems before 1/3/2019 

> Now, I want to solve the problems as quickly as possible, so what I can do is forked the code and do my business.

* The class in python can be used and run directly like this:

```python
class Solution:  
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
print (s.isMatch("ab", ".*c"))
```

* For the beginer, you may think the code is so ugly that there is only a class, the following will explain that:

> On the leetcode, what matters is only whether the function we type works, so the input is prepared well for us.
Thus, we only propose a module as the function, that will be enough.

* PROBLEMS
> 1. Can not understand the code in 30.py

* HOW TO PSUH THE CODE TO GITHUB?
>
```python
git add .
git commit -m "AC all the problems on leetcode before 1/3/2019"
git push -u origin master
```

