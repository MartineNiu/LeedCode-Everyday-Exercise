arr = list(map(int, input().split()))
cnt = int(input())

if sum(arr)<=cnt:
    print(-1)

else:
    left = 0
    right = max(arr)
    while left <= right:
        mid = (left+right)//2
        total = sum(i if i<=mid else mid for i in arr)
        if total<=cnt:
            value = mid
            left = mid+1
        else:
            right = mid-1

    print(value)

