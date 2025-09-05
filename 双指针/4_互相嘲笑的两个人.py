# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
    
#     if n == 1:
#         return 1
    
#     max_count = 1
#     current_count = 1
    
#     for i in range(1, n):
#         # 检查相邻关卡的分数差值是否相等
#         if a[i] - a[i-1] == b[i] - b[i-1]:
#             current_count += 1
#         else:
#             max_count = max(max_count, current_count)
#             current_count = 1
    
#     return max(max_count, current_count)

# print(solve())


