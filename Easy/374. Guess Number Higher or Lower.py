
class Solution(object):
    def guessNumber(self, n):
            left=0
            right=n
            while left<=right:
                mid=(right+left)//2
                result=guess(mid)
                if result==0:
                    return mid
                elif result==1:
                    left=mid+1
                else:
                    right=mid-1
            
