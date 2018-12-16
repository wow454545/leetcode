class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 每次循环，先取一个前面的值，在从后面选左右
        nums.sort()
        res=sum(nums[:3])
        m=abs(res-target)
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                temp=nums[i]+nums[l]+nums[r]
                if abs(res-target)>abs(temp-target):
                    res=temp
                elif target<temp:
                    r-=1
                else:
                    l+=1
        return res
s=Solution()
print(s.threeSumClosest([-1, 2, 1, -4],1))