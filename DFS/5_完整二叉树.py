MOD = 10**9+7

num = int(input())
tree_info = list(map(int,input().split()))

adj = [[] for _ in range(num)]
for i in range(num-1):
    parent = tree_info[i]-1
    child = i+1
    adj[parent].append(child)


