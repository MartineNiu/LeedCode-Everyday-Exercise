# 方法1：使用sys.stdin读取输入,结合for循环，常用
# 使用ctrl+Z结束输入

import sys
for line in sys.stdin:
    numbers = list(map(int, line.split()))
    print(sum(numbers))

# 方法2：使用try-except捕获EOFError异常
# while True:
#     try:
#         line = input()
#         numbers = list(map(int, line.strip().split()))
#         print(sum(numbers))
#     except EOFError:
#         break
