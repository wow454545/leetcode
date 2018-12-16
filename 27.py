class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=len(nums)
        if l==0:
            return 0
        i=0
        while i<l:
            if nums[i]==val:
                # pop() the index i element
                nums.pop(i)
                l-=1
            else:
                i+=1
        return len(nums)

s=Solution()
print(s.removeElement([3,2,2,3],3))