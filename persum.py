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

"""
1109.这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
"""
# 暴力解法，记录每一条贡献，构建二维表，按列求和
def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        m = len(bookings)
        mat = [[0] * n for _ in range(m)]
        for idx, (first, last, seat) in enumerate(bookings):
            l = first - 1
            r = last - 1
            for i in range(l, r+1):
                mat[idx][i] = seat
        ans = [sum(col) for col in zip(*mat)]
        return ans

# 差分数组 数组的后一项减前一项
def corpFlightBookings1(self, bookings: list[list[int]], n: int) -> list[int]:
    pass

"""
59.给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
"""
# ## 思路：边界收缩法, 维护四条边界：`top`：当前最上面一行`bottom`：当前最下面一行`left`：当前最左一列`right`：当前最右一列. 填充顺序固定：1. 上边：从左→右，填完 `top += 1`2. 右边：从上→下，填完 `right -= 1`3. 下边：从右→左（**需要判断 top <= bottom，防止只剩一行时重复填**），填完 `bottom -=1`  4. 左边：从下→上（**需要判断 left <= right，防止只剩一列时重复填**），填完 `left +=1`. 直到边界交叉，全部填完。

def generateMatrix(self, n: int) -> list[list[int]]:
        # 初始化n×n二维数组
        mat = [[0]*n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1

        while top <= bottom and left <= right:
            # 1. 上行：左 → 右
            for j in range(left, right + 1):
                mat[top][j] = num
                num += 1
            top += 1

            # 2. 右列：上 → 下
            for i in range(top, bottom + 1):
                mat[i][right] = num
                num += 1
            right -= 1

            # 3. 下行：右 → 左；只剩一行时不要再填
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    mat[bottom][j] = num
                    num += 1
                bottom -= 1

            # 4. 左列：下 → 上；只剩一列时不要再填
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    mat[i][left] = num
                    num += 1
                left += 1
        return mat

"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""
#(i,j), (n-j-1, i), (n-i-1, n-j-1), (j, n-i-1)
def rotate(self, matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            # 四个位置同时交换
            matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1] = \
            matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j]