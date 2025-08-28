from collections import defaultdict
n = int(input())
nums = list(map(int, input().split()))
count = 0
positions = defaultdict(list)
for idx, num in enumerate(nums):
    positions[num].append(idx)

for j in range(1,n-1):
    mid = nums[j]
    find = mid+1
    left = sum(1 for i in positions[find] if i < j)
    right = sum(1 for i in positions[find] if i > j)
    count += left * right

print(count)
