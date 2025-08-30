from collections import defaultdict

def max_diff(nums):
    n = len(nums)
    counter = defaultdict(int)
    left = right = 0
    max_length = 0
    while right <n:
        counter[nums[right]] += 1
        while counter[nums[right]]==2:
            counter[nums[left]]-=1
            left += 1
        max_length = max(max_length, right-left+1)
        right +=1
    return max_length

n = int(input())
nums = list(map(int, input().split()))
result = max_diff(nums)
print(result)

