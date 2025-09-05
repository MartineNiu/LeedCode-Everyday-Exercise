def count_intervals(a,x,k):
    n = len(a)
    divisable = [1 if num % x ==0 else 0 for num in a]

    left = 0
    right = 0
    count = 0
    total = 0
    for right in range(n):
        count += divisable[right]

        while left <= right and count > k:
            count -= divisable[left]
            left+=1
        
        if count == k:
            temp_left = left
            while temp_left <= right and divisable[temp_left]==0:
                temp_left +=1
            total += temp_left-left+1
    return total


a = list(map(int, input().split()))
x, k = map(int, input().split())
result = count_intervals(a,x,k)
print(result)
