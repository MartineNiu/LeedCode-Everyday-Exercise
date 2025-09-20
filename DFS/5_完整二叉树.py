MOD = 10**9+7

num = int(input())
tree_info = list(map(int,input().split()))
opt = list(map(int, input().split()))

adj = [[] for _ in range(num)]
for i in range(num-1):
    parent = tree_info[i]-1
    child = i+1
    adj[parent].append(child)

def cc(a, b, t):
    return (a+b) % MOD if t == 0 else (a*b) % MOD

def cal(u):
    if len(adj[u]) == 2:
        return cc(cal(adj[u][0]), cal(adj[u][1]), opt[u])
    return 1

print(cal(0))


