import sys

# 题目要求树的深度可能很大，增加递归深度限制，防止因递归过深而报错
sys.setrecursionlimit(10**6)

# --- 输入处理 ---
# 读取节点数量 n
n = int(input())
# 读取长度为 n 的颜色字符串，并去除首尾可能存在的空白字符
colors = input().strip()
# 初始化结果计数器，用于统计满足条件的子树数量
result = 0

# 创建邻接表来存储树的结构。adj[i] 是一个列表，包含所有与节点 i+1 相连的节点
adj = [[] for _ in range(n)]
# 循环 n-1 次，读取每一条边
for i in range(n-1):
    # 读取边的两个端点 u 和 v
    u, v = map(int, input().split())
    # 因为邻接表是0-based索引，而输入是1-based，所以需要减1
    # 无向图，所以两个节点的邻接列表都要添加对方
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

# --- 核心算法：深度优先搜索 (DFS) ---
def dfs(node, parent):
    """
    深度优先搜索函数，用于遍历树并检查每个子树的颜色构成。
    :param node: 当前正在访问的节点 (0-based index)
    :param parent: 当前节点的父节点 (0-based index)，用于防止DFS走回头路
    :return: 一个元组 (has_red, has_black)，布尔值，表示以`node`为根的子树中是否包含红色/黑色节点
    """
    # 声明 result 为全局变量，以便在函数内部修改它
    global result
    
    # 初始化当前节点为根的子树的颜色状态
    has_red = False
    has_black = False
    
    # 1. 首先检查当前节点自身的颜色
    if colors[node] == 'R':
        has_red = True
    else:
        has_black = True

    # 2. 遍历当前节点的所有邻居
    for neighbor in adj[node]:
        # 如果邻居不是父节点，说明它是子节点，对其进行递归调用
        if neighbor != parent:
            # 递归调用DFS，获取子节点为根的子树的颜色信息 (r, b)
            r, b = dfs(neighbor, node)
            
            # 3. 根据子树返回的结果，更新当前子树的颜色状态
            # 如果子树中包含红色，那么当前节点为根的子树也必然包含红色
            if r:
                has_red = True
            # 如果子树中包含黑色，那么当前节点为根的的子树也必然包含黑色
            if b:
                has_black = True
                
    # 4. 在遍历完所有子节点后，检查当前节点为根的整个子树是否满足条件
    # 如果这个子树同时包含了红色和黑色节点
    if has_red and has_black:
        # 那么就找到了一个满足条件的节点，结果加一
        result += 1
        
    # 5. 将当前节点为根的子树的颜色信息返回给它的父节点
    return has_red, has_black

# --- 程序入口 ---
# 从节点 0 (对应题目中的节点1) 开始进行DFS，-1表示初始节点没有父节点
dfs(0, -1)

# 打印最终结果
print(result)
