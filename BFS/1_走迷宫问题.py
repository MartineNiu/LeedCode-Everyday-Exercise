from collections import deque

# 创建一个空的队列
q = deque()

# 入队操作：append
q.append(10)  # 向队列中添加元素 10
q.append(20)  # 向队列中添加元素 20
q.append(30)  # 向队列中添加元素 30

# 获取队列的大小
print("队列大小:", len(q))  # 输出 3

# 查看队列的头部元素：[0] 直接取值
print("队列头部元素:", q[0])  # 输出 10

# 出队操作：popleft
q.popleft()  # 移除队列中的第一个元素

# 再次查看队列的头部元素
print("新的队列头部元素:", q[0])  # 输出 20

# 判断队列是否为空：empty
if len(q) == 0:
    print("队列为空")
else:
    print("队列不为空")
