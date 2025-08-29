def find(nums,target):
    p1 = 0
    p2 = n-1
    while p1 <p2:
        if nums[p1] + nums[p2]==target:
            return '{} {}'.format(p1+1,p2+1)
        elif nums[p1]+nums[p2]>target:
            p2-=1
        else:
            p1+=1
    return '-1'

n = int(input())
nums = list(map(int, input().split()))
target = int(input())
print(find(nums,target))