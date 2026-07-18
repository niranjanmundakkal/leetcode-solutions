class Solution(object):
    def findGCD(self, nums):
        maxi=max(nums)
        mini=min(nums)
        gcd=1
        for i in range(1,maxi+1):
            if mini%i==0 and maxi%i==0:
                gcd=max(gcd,i)
        return gcd

            