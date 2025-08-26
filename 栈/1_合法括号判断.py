# s = input().strip()
# stack = []
# for char in s:
#     if char == '(':
#         stack.append(char)
#     elif char == ')':
#         if not stack:
#             print('No')
#             exit(0) # 立即结束程序
#         stack.pop()
# if not stack:
#     print('Yes')
# else:
#     print('No')
        
        
# 上面的解答适合于只有一种左右括号，也就是说直接弹出
# 但不需要判断弹出的是否和右括号匹配
# 如果是多种括号，就需要注意匹配
s = input().strip()
mapping = {')':'(', ']':'[', '}':'{'}
stack = []
for char in s:
    if char in mapping.values():
        stack.append(char)
    else:
        if not stack or stack[-1] != mapping[char]:
            print('No')
            exit(0)
        stack.pop()

if not stack:
    print('Yes')
else:
    print('No')

    
