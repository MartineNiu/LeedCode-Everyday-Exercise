n = int(input())
arr = list(map(int, input().split()))
max_val = max(arr)
print(max_val)  # 输出数组中的最大值

indices = [i for i, x in enumerate(arr) if x == max_val]
print(' '.join(map(str, indices))) # 输出最大值的索引

# # 📘 Python内置函数：enumerate()

# # ✅ 用法：
# #     enumerate(iterable, start=0) 会将可迭代对象转化为 (index, value) 对的迭代器
# #     常用于遍历列表时同时获取元素和下标

# # 🧪 示例：
# arr = [10, 20, 30]
# for i, val in enumerate(arr):
#     print(f"下标 {i} 的值是 {val}")
# # 输出：
# # 下标 0 的值是 10
# # 下标 1 的值是 20
# # 下标 2 的值是 30

# # 📌 可选参数 start 可以指定起始下标：
# for i, val in enumerate(arr, start=1):
#     print(f"第 {i} 项是 {val}")
# # 输出下标从 1 开始计数

# # --------------------------------------------------

# # 📘 字符串方法：" ".join()

# # ✅ 用法：
# #     "分隔符".join(可迭代对象) 会将元素连接成一个字符串，中间用指定分隔符隔开
# #     常用于将列表中的字符串拼接成一行输出

# # 🧪 示例：
# names = ["Alice", "Bob", "Charlie"]
# result = ", ".join(names)
# print(result)
# # 输出：Alice, Bob, Charlie

# # 📌 如果列表中是整数，需要先转换为字符串：
# nums = [1, 2, 3]
# print(" ".join(map(str, nums)))
# # 输出：1 2 3

# # 🧠 常见场景：
# #     - 输出多个数字或字符串时格式化为一行
# #     - 与列表推导式配合使用，构造输出格式

# # --------------------------------------------------

# # 🧠 总结：
# #     - enumerate() 用于同时获取元素和下标
# #     - join() 用于将多个字符串合并为一个整体输出
# #     - 两者常在数组处理、格式化输出、查找类题目中组合使用
