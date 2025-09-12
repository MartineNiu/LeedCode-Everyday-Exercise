# 联通块：
# 1.联通性：任意两个顶点之间都能通过路径相互到达
# 2.极大性：一个联通顶点集无法再向其中添加任何其他顶点而仍然保持联通
MAX = 1001
adj = [[] for _ in range(MAX)]
visited = [False] * MAX

def dfs(node):
    visited[node] = True
    for neighbor in adj[node]:
        if visited[neighbor] is False:
            dfs(neighbor)

def main():
    n,m = map(int,input().split())
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    count = 0

    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)
            count += 1
    print(count)

main()