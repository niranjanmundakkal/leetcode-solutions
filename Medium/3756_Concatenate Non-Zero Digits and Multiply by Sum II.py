class Solution(object):
    def sumAndMultiply(self, s, queries):
        
    
        MOD = 10**9 + 7
        n = len(s)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        tree = [(0, 0, 0)] * (4 * n)   # (cnt, sum, val)

        def merge(a, b):
            c1, s1, v1 = a
            c2, s2, v2 = b
            return (c1 + c2, s1 + s2, (v1 * pow10[c2] + v2) % MOD)

        def build(node, l, r):
            if l == r:
                d = int(s[l])
                if d == 0:
                    tree[node] = (0, 0, 0)
                else:
                    tree[node] = (1, d, d)
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2
            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)
            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)
            return merge(left, right)

        build(1, 0, n - 1)

        ans = []
        for l, r in queries:
            cnt, sm, val = query(1, 0, n - 1, l, r)
            ans.append((val * sm) % MOD)

        return ans