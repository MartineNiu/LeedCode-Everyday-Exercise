def main():
    a = input().strip()
    b = input().strip()

    length = len(a)
    for i in range(length+1):
        a1 = a[:i]
        a2 = a[i:]
        c = a1+b+a2
        d = c[::-1]
        # 如果用reversed（）方法
        # d = ''.join(reversed(c))
        # reversed() 是一个内置函数，
        # 返回的是一个迭代器，不是字符串。
        # 需要把它转换回字符串，
        # 或者更简单地用切片反转字符串
        if d == c:
            return 'YES'
    return 'NO'
print(main())

