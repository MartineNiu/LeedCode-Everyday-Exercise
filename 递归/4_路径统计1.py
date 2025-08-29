def countPaths(i, j, n):
    if i >= n or j >= n:
        return 0
    if i == n-1 and j == n-1:
        return 1
    return countPaths(i + 1, j, n) + countPaths(i, j+1, n)

n = int(input())
print(countPaths(0, 0, n))