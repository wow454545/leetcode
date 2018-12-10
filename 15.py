class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        :答案很容易超时，看运气的
        """
        res=[]
        # 从小到大排序
        nums.sort()
        for i in range(len(nums)-1):
            left=i+1
            right=len(nums)-1
            while left<right:
                val=nums[i]+nums[left]+nums[right]
                if val==0 and [nums[i],nums[left],nums[right]] not in res:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    break
                elif val<0:
                    left+=1
                else:
                    right-=1
        return res
s=Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))