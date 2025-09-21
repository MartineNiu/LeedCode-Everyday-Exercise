import sys
sys.setrecursionlimit(200000)
n = int(input())
a = list(map(int, input().split()))
adj = [[] for _ in range (n)]

for i in range(n-1):
    u, v = map(int,input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

def dfs(node, father):
    total_add = 0
    total_sum = 0
    for neighbor in adj[node]:
        if neighbor != father:
            child_add, child_sum = dfs(neighbor, node)
            total_add += child_add
            total_sum += child_sum
    
    if a[node] < total_sum:
        total_add += total_sum -a[node]
        a[node] = total_sum

    return total_add, a[node]

result, _ = dfs(0, -1)
print(result)
