from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        n1,n2=len(s1),len(s2)
        if n1>n2:
            return False
        c1=Counter(s1)
        window=Counter(s2[:n1])
        if c1==window:
            return True
        for i in range(n1,n2):
            window[s2[i]]+=1
            window[s2[i-n1]]-=1
            if window[s2[i - n1]] == 0:
                del window[s2[i - n1]]

            if window == c1:
                return True

        return False