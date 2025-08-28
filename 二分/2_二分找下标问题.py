# 方法1 ：用二分法定位一个目标值，然后向左右扩展找边界
def find_idx(arr, target):
    result = [-1,-1]
    n = len(arr)
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid]==target:
            result = [mid, mid]
            p1 = p2 = mid # 找到后，不断往两边延伸
            while p1>=0 and arr[p1]==target:
                p1 -=1
            while p2<n and arr[p2] == target:
                p2 += 1
            result = [p1+2, p2]# 下标转化
            break
        elif arr[mid]>target:
            right = mid-1
        else:
            left = mid+1
    return result

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(q):
        target = int(input())
        result = find_idx(arr, target)
        print(" ".join(map(str, result)))

main()
    
# 方法2：二分法变形
# 对于左边界：
# 即使nums[mid] == target, right仍然左移 
# def find_first(A, x):
#     left, right = 0,len(A)-1
#     ans = -1
#     while left <= right:
#         mid = (left + right) //2
#         if A[mid] == x:
#             ans = mid
#             right = mid-1
#         elif A[mid] > x:
#             right = mid-1
#         else:
#             left = mid+1
#     return ans

# def find_last(A, x):
#     left, right = 0,len(A)-1
#     ans = -1
#     while left <= right:
#         mid = (left + right) //2
#         if A[mid] == x:
#             ans = mid
#             left = mid+1
#         elif A[mid] > x:
#             right = mid-1
#         else:
#             left = mid+1
#     return ans

# def main():
#     n, q = map(int, input().split())
#     A = list(map(int, input().split()))
#     for _ in range(q):
#         x = int(input())
#         first = find_first(A, x)
#         last = find_last(A, x)
#         if first == -1:
#             print("-1 -1")
#         else:
#             print(f"{first + 1} {last + 1}")  # 转为 1-based 下标
# main()