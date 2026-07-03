class Solution(object):
    def intersection(self, nums1, nums2):
        s1=set(nums1)
        ans=set()
        
        for num in nums2:
            if num in s1:
                ans.add(num)
        return list(ans)
