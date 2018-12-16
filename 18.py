class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lens=len(nums)
        dic={}
        res=set()
        nums.sort()
        # 计算每一个数和其后面的所有数的和，并将结果存储在map中
        for i in range(lens-1):
            for p in range(i+1,lens):
                key=nums[i]+nums[p]
                if key not in dic:
                    dic[key]=[(i,p)]
                else:
                    dic[key].append((i,p))
        for i in range(2,lens-1):
            for p in range(i+1,lens):
                pre=target-nums[i]-nums[p]
                if pre in dic:
                    for index in dic[pre]:
                        # 判断前面的两个索引都小于后面的索引才符合条件
                        if index[1]<i:
                            res.add((nums[index[0]],nums[index[1]],nums[i],nums[p]))
        return [list(i) for i in res]