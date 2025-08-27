from collections import defaultdict

n, q = map(int, input().split())
nums = list(map(int, input().split()))
positions = defaultdict(list)

for idx, num in enumerate(nums):
    positions[num].append(idx+1)

for _ in range(q):
    x, k = map(int, input().split())
    if k>len(positions[x]):
        print(-1)
    else:
        print(positions[x][k-1])
        