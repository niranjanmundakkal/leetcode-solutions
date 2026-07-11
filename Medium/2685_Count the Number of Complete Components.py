class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1

        cnt_edge = [0] * n
        sz = [1] * n
        par = list(range(n))

        def find(node):
            if par[node] == node:
                return node
            par[node] = find(par[node])
            return par[node]

        def merge(u, v):
            rootU = find(u)
            rootV = find(v)

            if rootU == rootV:
                cnt_edge[rootU] += 1
                return

            if sz[rootU] > sz[rootV]:
                rootU, rootV = rootV, rootU

            par[rootU] = rootV
            sz[rootV] += sz[rootU]
            cnt_edge[rootV] += cnt_edge[rootU] + 1

        for u, v in edges:
            merge(u, v)

        ans = 0
        vis = set()

        for i in range(n):
            p = find(i)
            if p in vis:
                continue
            vis.add(p)

            if cnt_edge[p] == (sz[p] * (sz[p] - 1)) // 2:
                ans += 1

        return ans