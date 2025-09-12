# 联通块：
# 1.联通性：任意两个顶点之间都能通过路径相互到达
# 2.极大性：一个联通顶点集无法再向其中添加任何其他顶点而仍然保持联通
MAX = 1001
adj = [[] for _ in range(MAX)]
visited = [False] * MAX

def dfs(node):
    visited[node] = True #标记当前节点为已经访问
    for neighbor in adj[node]:# 遍历邻居
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

'''
一次 dfs() 调用的作用：确实会把从起始点可达的所有节点都标记为 visited[i] = True

main() 中的 dfs() vs 函数内的 dfs()：

main() 中的 dfs()：是每个连通块的"入口点"，开始探索一个新的连通块
函数内的 dfs()：是递归调用，用于深度遍历当前连通块内的其他节点

'''