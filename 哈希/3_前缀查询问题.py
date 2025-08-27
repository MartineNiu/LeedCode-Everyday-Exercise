# from collections import defaultdict
# n = int(input())
# nums = list(map(int, input().split()))
# positions = defaultdict(list)

# for idx, num in enumerate(nums):
#     positions[num].append(idx +1)

# result = []
# for i in range(1,n+1):
#     count = 0
#     position_i = positions[i]
#     count = sum(1 for x in position_i if x <= i)
#     result.append(count)

# print(' '.join(map(str, result)))

# 还有更简洁的方法，直接边遍历，边print
n = int(input())
a = list(map(int, input().split()))
counts = {i:0 for i in range(1,n+1)}
for i in range(n):
    num = a[i]
    counts[num] += 1
    if i > 0:
        print(' ',end = '')
    print(counts[i+1],end = '')