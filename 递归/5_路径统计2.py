countpath = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x,y,steps,n,sx,sy,ex,ey,k):
    global countpath

    if x==ex and y==ey:
        countpath += 1

    if steps == k:
        return
    
    for dir in range(4):
        newx = x+dx[dir]
        newy = y+dy[dir]
        if 1 <= newx <= n and 1<=newy<=n:
            dfs(newx, newy, steps +1, n, sx, sy, ex, ey, k)


n = int(input())
sx,sy,ex,ey = map(int, input().split())
k = int(input())
dfs(sx, sy, 0, n, sx,sy,ex,ey,k)
print(countpath)