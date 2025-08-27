# 方法1：入栈前判断
# def elimate(arr):
#     stack = []
#     for i in arr:
#         if len(stack)<=1 or stack[-1]!=i or stack[-2]!=i:
#             stack.append(i)
#         else:
#             stack.pop()
#             stack.pop()
#     return stack

# arr = list(map(int, input().split()))
# stack = elimate(arr)
# if not stack:
#     print('[]')
# else:
#     print(' '.join(map(str, stack))) 


# 方法2：入栈后判断
def elimate(arr):
    stack = []
    for i in arr:
        stack.append(i)
        if len(stack)>=3 and stack[-1]==stack[-2]==stack[-3]==i:
            stack.pop()
            stack.pop()
            stack.pop()
    return stack

arr = list(map(int, input().split()))
result = elimate(arr)
if not result:
    print('[]')
else:
    print(' '.join(map(str, result)))