class Solution(object):
    def reverseWords(self, s):
        
        se=list(s.split())
        l=0
        r=len(se)-1
        while l<r:
            
            se[l],se[r]=se[r],se[l]
            l+=1
            r-=1
        return " ".join(se)
        