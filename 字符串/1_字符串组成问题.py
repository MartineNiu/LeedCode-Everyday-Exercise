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

    while len_b >0:
        if a != b[:len_a]:
            return 'No'
        else:
            b = b[len_a:]
            len_b = len(b)
    return 'Yes'

result = a_b()
print(result)
        


