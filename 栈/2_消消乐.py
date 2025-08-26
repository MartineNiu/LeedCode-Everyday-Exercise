def elimate(arr):
    stack = []
    for i in arr:
        if len(stack)<=1 or stack[-1]!=i or stack[-2]!=i:
            stack.append(i)
        else:
            stack.pop()
            stack.pop()
    return stack

arr = list(map(int, input().split()))
stack = elimate(arr)
if not stack:
    print('[]')
else:
    print(' '.join(map(str, stack))) 