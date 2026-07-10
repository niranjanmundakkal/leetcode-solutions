class Solution(object):
    def findMaxAverage(self, nums, k):
        wsum=sum(nums[:k])
        maxsum=wsum
        for i in range(k,len(nums)):
            wsum+=nums[i]-nums[i-k]
            maxsum=max(maxsum,wsum)
        return float(maxsum)/k