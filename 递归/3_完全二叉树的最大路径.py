def maxPathSum(arr, index, n):
    left_index = 2*index +1
    right_index = 2*index +2

# 如果左右子节点的索引都超出了数组范围，
# 说明当前节点是叶子节点，直接返回它的值
    if left_index >=n and right_index >=n:
        return arr[index]
    
    left_sum = 0
    right_sum = 0

    if left_index < n:
        left_sum = maxPathSum(arr,left_index,n)
    
    if right_index < n:
        right_sum = maxPathSum(arr, right_index,n)

    return arr[index] + max(left_sum, right_sum)

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    res = maxPathSum(arr, 0, n)
    print(res)

main()