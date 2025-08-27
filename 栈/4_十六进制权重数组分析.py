# n = int(input())
# arr = list(map(int,input().split()))
# hex_list = [format(x,'X') for x in arr]
# # print(hex_list)
# hex_weights = {ch: int(ch, 16) for ch in "0123456789ABCDEF"}
# weight = []
# for i in hex_list:
#     sum = 0
#     for char in i:
#         sum += hex_weights[char]
#     weight.append(sum)
# result = [-1]*len(arr)
# stack = []
# top = -1
# for idx, value in enumerate(weight):
#     if not stack:
#         stack.append(idx)
#         top+=1
#     elif value <= weight[stack[-1]]:
#         stack.append(idx)
#         top += 1
#     else:
#         while top >=0 and weight[stack[top]]<value:
#             result[stack[top]]=idx
#             stack.pop()
#             top -= 1
#         stack.append(idx)
#         top += 1
# print(' '.join(map(str,result)))


# 有更简洁的写法
n = int(input())
arr = list(map(int, input().split()))

# 十六进制字符串列表
hex_list = [format(x, 'X') for x in arr]

# 十六进制字符权重映射
hex_weights = {ch: int(ch, 16) for ch in "0123456789ABCDEF"}

# 计算每个数字的权重
weight = []
for hex_str in hex_list:
    total = sum(hex_weights[ch] for ch in hex_str)
    weight.append(total)

# 单调栈求右侧第一个权重大于当前的索引
result = [-1] * n
stack = []

for idx, value in enumerate(weight):
    while stack and weight[stack[-1]] < value:
        result[stack.pop()] = idx
    stack.append(idx)

print(' '.join(map(str, result)))

'''
python 中format函数的用法
 
格式符	    含义	       示例(x=255)       输出
'b'	  二进制(binary)	format(255, 'b')	'11111111'
'o'	  八进制(octal)	    format(255, 'o')	'377'
'd'	  十进制(decimal)	format(255, 'd')	'255'
'x'	  十六进制（小写）	 format(255, 'x')	 'ff'
'X'	  十六进制（大写）	 format(255, 'X')	 'FF'

字符串按照指定进制转化

int('FF', 16)   # 十六进制 → 255
int('1010', 2)  # 二进制 → 10
int('12', 8)    # 八进制 → 10


'''