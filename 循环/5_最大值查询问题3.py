n, m = map(int, input().split())
matrix = []
for _ in range(n):
    arr = list(map(int, input().split()))
    matrix.append(arr)
 
q = int(input())
for _ in range(q):
    x1, y1, x2, y2 = map(int,input().split())
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    max_val = matrix[x1][y1]
    for i in range(x1,x2+1):
        for j in range(y1, y2+1):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
            else:
                continue
    print(max_val)
 