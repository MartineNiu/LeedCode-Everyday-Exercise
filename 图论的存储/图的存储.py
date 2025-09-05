# 判断两站图是否完全相同
'''
两种图的存储方式：

1、邻接矩阵（适合稠密图）
# 使用二维数组matrix[i][j]表示边是否存在
# 空间复杂度高，但访问方便
def create_adj_matrix(n):
    return [[0]*(n+1) for _ in range(n+1)]
def add_edge(adj_matrix, u, v):
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1（无向图两边都得1）

2、邻接表（适合稀疏图）
# 使用字典或列表存储每个顶点的邻居
# 空间效率高，适合大规模图
adj_list = {i:[] for i in range(MAX)}
def add_edge(adj_list, u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)
'''

#解题思路
# 将图 A 的邻接矩阵转换为邻接表 adj_a
# 读取图 B 的邻接表 adj_b
# 对每个节点的邻接表排序
# 比较 adj_a[i] == adj_b[i] 是否成立

# 读取节点数
n = int(input())

# 图A：邻接矩阵转邻接表
adj_a = {i:[] for i in range(1,n+1)}
for i in range(1,n+1):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j]==1:
            adj_a[i].append(j+1)

# 图B：直接读取邻接表
adj_b = {i:[] for i in range(1,n+1)}
for i in range(1,n+1):
    row = list(map(int, input().split()))
    adj_b[row[0]].extend(row[2:])

for i in range(1,n+1):
    adj_a[i].sort()
    adj_b[i].sort()

same = True
for i in range(1,n+1):
    if adj_a[i]!= adj_b[i]:
        same = False
        break

print('YES' if same else 'NO')