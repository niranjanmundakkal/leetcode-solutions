class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for v in nums:
            freq[v] += 1

        g = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            m = 0
            for k in range(d, mx + 1, d):
                m += freq[k]
                g[d] -= g[k]            
            g[d] += m * (m - 1) // 2    

        s = list(accumulate(g))        
        return [bisect_right(s, q) for q in queries]