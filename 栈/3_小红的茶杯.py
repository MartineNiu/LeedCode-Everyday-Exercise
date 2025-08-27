nums = list(map(int, input().split()))
stack = []  # 用列表模拟栈
for x in nums:
    while True:
        flag = False
        tmp_sum = 0
        for i in range(len(stack) - 1, -1, -1):
            tmp_sum += stack[i]
            if tmp_sum == x:
                stack = stack[:i]
                # 新的数字是 x + tmp_sum
                x += tmp_sum
                flag = True
                break
        # 如果没有发生合并，退出 while 循环
        if not flag:
            break
    # 把当前数字压入栈
    stack.append(x)
# 输出栈顶到栈底

stack = stack[::-1]
print(' '.join(map(str, stack)))