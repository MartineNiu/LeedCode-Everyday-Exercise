n, q = map(int, input().split())
nums = list(map(int, input().split()))
dict = {}
for num in nums:
    if num in dict:
        dict[num]+=1
    else:
        dict[num]=1
    
for i in range(q):
    target = int(input())
    if target in dict:
        print(dict[target])
    else:
        print(0)

