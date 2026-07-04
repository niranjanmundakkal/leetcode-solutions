class Solution(object):
    def maxSubArray(self, nums):
        curr=nums[0]
        m=nums[0]
        for i in range(1,len(nums)):
            curr=max(nums[i],nums[i]+curr)
            m=max(m,curr)
        return m