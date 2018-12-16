class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        # the comment should be english or fails the running
        # the method is named retrospective way
        def backtract(s='',left=0,right=0):
            if len(s)==2*n:
                # every s is one solution in ans
                # when the length of s equals n, one solution is done.
                ans.append(s)
                return
            # when left parenthesis is less than n, we can add it
            if left<n:
                backtract(s+'(',left+1,right)
            # only when left is more than right,
            # can we add right parenthesis once
            if left>right:
                backtract(s+')',left,right+1)

        backtract()
        return ans

s=Solution()
print(s.generateParenthesis(3))