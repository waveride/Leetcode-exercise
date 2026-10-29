"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
"""
# #前缀和 + 哈希表,遍历到位置 j，当前前缀和是 `pre_sum_j`
# 只要前面曾经出现过 `pre_sum_j - k` 这个前缀和，就说明：
# 中间这一段子数组和 = k 哈希表存：`key = 前缀和，value = 这个前缀和出现过多少次`

def subarraySum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    pre_sum = 0
    sum_map = defaultdict(int)
    sum_map[0] = 1
    count = 0

    for num in nums:
        pre_sum += num
        if pre_sum - k in sum_map:
            count += sum_map[pre_sum-k]
            
        sum_map[pre_sum]+=1
    return count

"""
定一个整数数组  nums，处理以下类型的多个查询:

计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
实现 NumArray 类
"""
# 前缀和（标准答案，考点）
# - 初始化（`__init__`）：提前算好前缀和数组，O (n)
# - 每次查询：`pre[right+1] - pre[left]`，直接返回，O (1)
# - 优点：查询极快，适合大量查询
# - 缺点：要多占一点内存存前缀和数组
class NumArray:
    def __init__(self, nums: list[int]):

        self.pre = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.pre[i+1]=self.pre[i]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1] - self.pre[left]