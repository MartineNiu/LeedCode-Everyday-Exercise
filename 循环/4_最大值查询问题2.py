# 写法一：先对子数组遍历一次求出最大值，然后进行第二次遍历，记录最大值下标
# n = int(input()) # 数组大小
# arr = list(map(int, input().split())) # 读取数组元素
# q = int(input()) # 查询次数

# for _ in range(q):
#     l, r = map(int, input().split())
#     max_value = max(arr[l-1:r])
#     print(max_value)
#     indices = [i+l for i, val in enumerate(arr[l-1:r]) if val == max_value]
#     print(' '.join(map(str, indices)))

#写法二：进行一次遍历，边比较边记录
n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    l, r = map(int, input().split())
    l-=1
    r-=1
    max_val = arr[l]
    indices = [l+1]
    for i in range(l,r+1):
        if arr[i]>max_val:
            
