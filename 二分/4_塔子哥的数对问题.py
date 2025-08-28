# 哈希表计数
from collections import Counter

def count_pairs(arr, c):
    freq = Counter(arr)
    res = 0
    for a in arr:
        res += freq.get(a-c, 0)
    return res

n = int(input())
arr = list(map(int, input().split()))
c = int(input())
result = count_pairs(arr,c)
print(result)


