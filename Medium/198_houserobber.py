class Solution(object):
    def rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        prev1=0
        prev2=0
        for num in nums:
            curr=max(prev2+num,prev1)
            prev2=prev1
            prev1=curr
        return prev1