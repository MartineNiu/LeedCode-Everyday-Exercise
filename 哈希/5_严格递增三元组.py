# 方法1：先遍历一遍，把数组各个数字出现的索引记录
# 遍历每个元素，寻找比该元素大1的元素的字典里面有多少索引
# 是分别位于该元素索引两侧的，然后相乘累加

# from collections import defaultdict
# n = int(input())
# nums = list(map(int, input().split()))
# count = 0
# positions = defaultdict(list)
# for idx, num in enumerate(nums):
#     positions[num].append(idx)

# for j in range(1,n-1):
#     mid = nums[j]
#     find = mid+1
#     left = sum(1 for i in positions[find] if i < j)
#     right = sum(1 for i in positions[find] if i > j)
#     count += left * right
# print(count)

#方法二
from collections import defaultdict

def main():
    n = int(input())
    res = 0 
    count_left = defaultdict(int) 
    count_right = defaultdict(int) 
    a = list(map(int, input().split()))
    for i in a:
        count_right[i] += 1 # 统计每个元素的频率
    
    for i in a:
        t = i + 1 # 计算t = a[j] + 1
        res += count_left[t] * count_right[t] # 计算符合条件的三元组数量
        count_left[i] += 1 # 更新count_left
        count_right[i] -= 1 # 更新count_right
    
    print(res)

if __name__ == "__main__":
    main()

