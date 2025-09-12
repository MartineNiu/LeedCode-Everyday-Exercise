n, m = map(int,input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    adj[u].append(v)
s, t = map(int, input().split())
'''
这是一个自顶向下的递归思路，核心思想是：从当前节点到目标节点的路径数 = 所有相邻节点到目标节点的路径数之和

递归的三个关键部分
1\递归边界（Base Case）
if u == t:
    return 1
当到达目标节点时，找到了一条路径，返回1

2\递归分解（Recursive Case）
for v in adj[u]:
    res += dfs(v)
遍历当前节点的所有邻接节点，累加从每个邻接节点到目标的路径数

3\合并结果
return res
'''

def dfs(u):
    if u == t:
        return 1
    res = 0
    for v in adj[u]:
        res += dfs(v)
    return res

res = dfs(s) 
print(res)        