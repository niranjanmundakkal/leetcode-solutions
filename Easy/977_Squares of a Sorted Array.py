class Solution(object):
    def sortedSquares(self, nums):
        n=len(nums)
        ans=[0]*n
        l=0
        r=n-1
        pos=n-1
        while l<=r:
            left=nums[l]*nums[l]
            right=nums[r]*nums[r]
            if left>right:
                ans[pos]=left
                l+=1
            else:
                ans[pos]=right
                r-=1
            pos-=1
        return ans

        