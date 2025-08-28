# 这个函数用来检查是否可以凑出来k套
def check(a, b, c, x, y, k):
    red_left = a - k
    b_new = b + red_left//x
    if b_new < k:
        return False
    b_left = b_new-k

    c_new = c+ b_left//y
    if c_new<k:
        return False
    else:
        return True

def  solve(a, b, c, x, y):
    left = 0
    right = a
    ans = 0
    while left <= right:
        mid = (left + right)//2
        if check(a,b,c,x,y,mid):
            ans = mid
            left = mid+1
        else:
            right = mid-1
    return ans

def main():
    n = int(input())
    for _ in range(n):
        a, b, c, x, y = map(int, input().split())
        result = solve(a, b, c, x, y)
        print(result)

main()