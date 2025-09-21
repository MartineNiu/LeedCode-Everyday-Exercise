import sys

# 题目数据量较大，树的深度可能很深，增加Python的递归深度限制，防止递归过深导致程序崩溃
sys.setrecursionlimit(200000)

# --- 输入处理 ---
# 读取节点数量 n
n = int(input())
# 读取 n 个节点的初始权值，存入列表 a (注意这是0-based索引)
a = list(map(int, input().split()))
# 创建邻接表 adj，用于存储树的结构。adj[i] 将包含所有与节点 i+1 相连的节点的索引
adj = [[] for _ in range (n)]

# 循环 n-1 次，读取所有边，并构建邻接表
for i in range(n-1):
    # 读取一条边的两个端点 u 和 v (1-based)
    u, v = map(int,input().split())
    # 将边信息存入邻接表。因为是无向图，所以两个节点的邻接列表都要添加对方。
    # 索引需要减1，以匹配Python的0-based列表索引。
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

# --- 核心算法：深度优先搜索 (DFS) ---
def dfs(node, father):
    """
    深度优先搜索函数，采用后序遍历（自底向上）的方式解决问题。
    对于每个节点，它计算出要使以它为根的子树成为“奇妙树”，需要进行的操作次数，
    并返回这个操作次数以及该节点调整后的新权值。

    :param node: 当前正在访问的节点 (0-based index)
    :param father: 当前节点的父节点 (0-based index)，用于防止DFS时走回头路
    :return: 一个元组 (total_add, final_node_value)
             - total_add: 使以`node`为根的整个子树满足条件的【最小总操作数】
             - final_node_value: `node`节点为了满足条件而调整后的【最终权值】
    """
    # 初始化当前子树的总操作数
    total_add = 0
    # 初始化当前节点的所有直接子节点的权值之和
    children_sum = 0
    
    # 1. 递归处理所有子节点（后序遍历的核心）
    # 遍历当前节点的所有邻居
    for neighbor in adj[node]:
        # 如果邻居不是父节点，那它就是子节点
        if neighbor != father:
            # 对子节点进行递归调用，获取使子树满足条件的“操作数”和子节点“调整后的权值”
            child_add, child_final_value = dfs(neighbor, node)
            
            # 累加来自子树的操作数
            total_add += child_add
            # 累加子节点调整后的最终权值
            children_sum += child_final_value
            
    # 2. 处理当前节点
    # 在所有子节点都处理完毕后，检查当前节点是否满足条件
    # 条件：当前节点的权值 >= 其所有子节点调整后的权值之和
    if a[node] < children_sum:
        # 如果不满足，计算需要增加的权值（即操作数）
        needed_add = children_sum - a[node]
        # 将这些操作数累加到总操作数中
        total_add += needed_add
        # “逻辑上”将当前节点的权值更新为满足条件的最小值
        a[node] = children_sum

    # 3. 返回结果给父节点
    # 返回这个子树的总操作数，以及当前节点调整后的最终权值
    # 父节点需要这个最终权值来进行自己的计算
    return total_add, a[node]

# --- 程序入口 ---
# 从根节点 0 (对应题目中的节点1) 开始进行DFS，-1表示根节点没有父节点
# 我们只需要最终的总操作数，所以用 _ 忽略返回的根节点最终权值
result, _ = dfs(0, -1)

# 打印最少需要的总操作次数
print(result)
