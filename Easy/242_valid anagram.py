class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        d1={}
        d2={}
        for ch in s:
            d1[ch]=d1.get(ch,0)+1
        for ch in t:
            d2[ch]=d2.get(ch,0)+1
        return d1==d2