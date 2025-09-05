n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pa = pb = 0
while pa < n and pb < m:
    if a[pa] == b[pb]:
        pa+=1
        pb+=1
    else:
        pb+=1


print('YES' if pa == n else 'NO')