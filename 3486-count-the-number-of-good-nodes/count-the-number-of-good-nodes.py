class Solution:
    def countGoodNodes(self, e: List[List[int]]) -> int:
        def dfs(n, p):
            t_s = 1
            c_s = []
            for c in t[n]:
                if c != p:
                    s = dfs(c, n)
                    t_s += s
                    c_s.append(s)
            if len(set(c_s)) <= 1:
                gn[0] += 1
            return t_s
        t = defaultdict(list)
        for u, v in e:
            t[u].append(v)
            t[v].append(u)
        gn = [0]
        dfs(0, -1)
        return gn[0]