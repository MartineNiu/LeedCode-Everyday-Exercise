import sys
sys.setrecursionlimit(10**6)

n = int(input())
colors = input().strip()
result = 0

adj = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

def dfs(node, parent):
    global result
    result = 0
    has_red = has_black = False
    if colors[node] == 'R':
        has_red = True
    else:
        has_black = True

    for neighbor in adj[node]:
        if neighbor != parent:
            r, b = dfs(neighbor,node)
            if r:
                has_red = True
            if b:
                has_black = True
    if has_red and has_black:
        result+=1
    return has_red, has_black

dfs(0,-1)
print(result)
