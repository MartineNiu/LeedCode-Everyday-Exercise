# 方法1：做减法，依次去掉b中的元素a，一旦有不一样就return
# def a_b():
#     a = input().strip()
#     b = input().strip()
#     len_a = len(a)
#     len_b = len(b)  

#     if len_b % len_a != 0:
#         return 'No'

#     while len_b >0:
#         if a != b[:len_a]:
#             return 'No'
#         else:
#             b = b[len_a:]
#             len_b = len(b)
#     return 'Yes'

# result = a_b()
# print(result)
        
# 方法2：做加法，将a不断复制，然后判断是否一样
def a_b():
    a = input().strip()
    b = input().strip()
    len_a = len(a)
    len_b = len(b)

    if len_b % len_a != 0:
        return 'No'
    
    k = len_b // len_a
    a = a * k
    if a == b:
        return 'Yes'
    else:
        return 'No'
    
print(a_b())


# split 和 strip的用法（坑）
'''
s = "a b c"
s.split()  # 默认按空格拆分 → ['a', 'b', 'c']

s.split(',')     # 按逗号分割
s.split(' ')     # 只按单个空格分割（多个空格不会合并）
s.split('\n')    # 按换行符分割

s = "  hello world  "
s.strip()  # → "hello world"

去除字符串首尾的空白字符（空格、\t、\n）

不影响中间的空格

s.lstrip()  # 去除左侧空白
s.rstrip()  # 去除右侧空白
s.strip(',')  # 去除首尾的逗号（不是空格）
'''