class Solution(object):
    def arrayRankTransform(self, arr):
        r={}
        sarr=sorted(set(arr))
        for i in range(len(sarr)):
            r[sarr[i]]=i+1
        ans=[]
        for  num in arr:
            ans.append(r[num])
        return ans