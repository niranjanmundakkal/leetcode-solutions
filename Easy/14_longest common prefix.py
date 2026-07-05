class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        f=strs[0]
        l=strs[-1]
        i=0
        while i<len(f) and i<len(l) and f[i]==l[i]:
            i+=1
        return f[:i]

        