class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        s=0
        for f in range(1,len(nums)):
            # remember the different elements in the nums start from the beginning,
            # and the s would be the sum different elements
            if nums[s]!=nums[f]:
                s+=1
                nums[s]=nums[f]
        # due to the length of the final nums is defined to be s+1, so the result is what we want.
        return s+1