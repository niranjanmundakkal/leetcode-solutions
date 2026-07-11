from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need=Counter(p)
        window=Counter()
        left=0
        ans=[]
        for right in range(len(s)):
            window[s[right]]+= 1
            if right-left+1>len(p):
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
            if window==need:
                ans.append(left)
        return ans