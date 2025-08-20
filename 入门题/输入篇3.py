# 方法1：使用sys.stdin读取输入,结合for循环，常用
# 使用ctrl+Z结束输入
# strip()方法用于去除字符串两端的空白字符
# map()函数将输入的字符串转换为整数列表

import sys
for line in sys.stdin:
    numbers = list(map(int, line.strip().split()))
    print(sum(numbers))


# 方法2：使用try-except捕获EOFError异常
# while True:
#     try:
#         line = input()
#         numbers = list(map(int, line.strip().split()))
#         print(sum(numbers))
#     except EOFError:
#         break
