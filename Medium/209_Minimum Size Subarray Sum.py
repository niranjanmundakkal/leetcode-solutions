class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        curr_sum=0
        ans=float('inf')
        for r in range(len(nums)):
            curr_sum+=nums[r]
            while curr_sum>=target:
                ans=min(ans,r-l+1)
                curr_sum-=nums[l]
                l+=1
        return  0 if ans==float('inf') else ans

        