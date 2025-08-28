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
    
