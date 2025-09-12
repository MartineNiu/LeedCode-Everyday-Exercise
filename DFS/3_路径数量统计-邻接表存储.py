n, m = map(int,input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    adj[u].append(v)
s, t = map(int, input().split())


def dfs(u):
    if u == t:
        return 1
    res = 0
    for v in adj[u]:
        res += dfs(v)
    return res

res = dfs(s) 
print(res)        