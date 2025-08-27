# 双层循环，会超时
# n = int(input())
# nums = list(map(int,input().split()))
# count = 0
# for i in range(n):
#     for j in range(i+1,n):
#         if i+j+2 == nums[i]+nums[j]:
#             count +=1

# print(count)


# 方法2，维护一个字典，键是Pi-i ,值是pi-i等于某个值的数量

n = int(input())
nums = list(map(int,input().split()))
diff_count = {}
count = 0
for idx, num in enumerate(nums):
    diff = idx+1-num
    if -diff in diff_count:
        count += diff_count[-diff]

    if diff in diff_count:
        diff_count[diff]+=1
    else:
        diff_count[diff] = 1

print(count)

