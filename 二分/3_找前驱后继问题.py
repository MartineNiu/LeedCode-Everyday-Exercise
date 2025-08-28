def find_left(arr, target):
    left, right = 0, len(arr)-1
    ans = -1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] < target:
            ans = arr[mid]
            left = mid +1
        else:
            right = mid-1
    return ans

def find_right(arr,target):
    left, right = 0, len(arr)-1
    ans = -1
    while left <= right:
        mid = (left+ right)//2
        if arr[mid]>target:
            ans = arr[mid]
            right = mid-1
        else:
            left = mid+1
    return ans

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(q):
        target = int(input())
        max_val = find_left(arr, target)
        min_val = find_right(arr, target)
        print(f"{max_val} {min_val}")

main()