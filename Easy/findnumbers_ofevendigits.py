class Solution(object):
    def evendig(self,num):
        count=0
        while num>0:
            d=num%10
            count=count+1
            num/=10
        
        return (count&1)==0
    

    def findNumbers(self, nums):
        ecount=0
        for num in nums:
            if self.evendig(num):
                ecount+=1
        return ecount
        