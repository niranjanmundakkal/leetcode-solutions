class Solution(object):
    def maxArea(self, height):
       l=0
       r=len(height)-1
       ans=0
       
       while l<r:
            area=(r-l)*min(height[l],height[r])
            ans=max(area,ans)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
       return ans
        