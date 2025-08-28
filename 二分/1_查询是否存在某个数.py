# 如果把二分法判断函数直接集成到主函数，会面临：
# 只能用print，不能return，否则会导致中途退出
# 因此需要额外加一个found标志

#  def main():
#     n, q = map(int, input().split())
#     nums = list(map(int, input().split()))
#     for _ in range(q):
#         target = int(input())
#         left = 0
#         right = n-1
#         found = False
#         while left<=right:
#             mid = (left + right)//2
#             if nums[mid]==target:
#                 print ('YES')
#                 found = True
#                 break
#             elif nums[mid]>target:
#                 right = mid-1
#             else:
#                 left = mid+1
#         if not found:
#             print('NO')
# main()

# 方法二：把二分法判断集成到另外一个函数里
def binary_search(nums, target):
    n = len(nums)
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid]==target:
            return True
        elif nums[mid] > target:
            right = mid -1
        else:
            left = mid+1
    return False
    
def main():
    n, q = map(int,input().split())
    nums = list(map(int, input().split()))
    for _ in range(q):
        target = int(input())
        if binary_search(nums, target):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
