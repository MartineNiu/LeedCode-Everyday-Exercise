class Solution:
    def twoSum(self, nums, target) :
        # 创建一个哈希表来存储元素及其下标 
        num_to_index = {}
        # 遍历数组 
        for i, num in enumerate(nums):
            # 计算需要的补数 
            complement = target - num 
            # 如果补数在哈希表中，返回对应的下标 
            if complement in num_to_index:
                return [num_to_index[complement], i]
            # 否则，将当前元素及其下标存入哈希表 
            num_to_index[num] = i 
        # 如果没有找到，返回空列表（根据题目，这种情况不会发生）
        return []
 
# 输入处理 
n, target = map(int, input().split())
nums = list(map(int, input().split()))
 
# 创建 Solution 类的实例并调用 two_sum 方法 
solution = Solution()
result = solution.twoSum(nums,  target)
 
# 输出结果 
print(result[0], result[1])

