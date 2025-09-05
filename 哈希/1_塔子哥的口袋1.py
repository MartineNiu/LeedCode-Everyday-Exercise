# n, q = map(int, input().split())
# nums = list(map(int, input().split()))
# dict = {}
# for num in nums:
#     if num in dict:
#         dict[num]+=1
#     else:
#         dict[num]=1
    

# # 可以用更pythonic的风格
# # freq = {}
# # for num in nums:
# #     freq[num] = freq.get(num,0)+1


# for i in range(q):
#     target = int(input())
#     print(dict.get(target,0))


from collections import Counter
n, q = map(int, input().split())
nums = list(map(int, input().split()))
counter = Counter(nums)

for _ in range(q):
    target = int(input())
    print(counter.get(target,0))