"""
回溯模板
1.确定backtrack的输入，一般是start的索引
2.确认中止条件
3.确定单层的搜索逻辑，记得最后pop
4.考虑剪枝，避免无用循环
"""


"""
39给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
"""
def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []
        total = 0

        def backtrack(start, total):
            if total > target:
                return
            if total == target:
                res.append(path.copy())

            for i in range(start, len(candidates)):
                num = candidates[i]
                path.append(num)

                backtrack(i, total+num)
                path.pop()

        backtrack(0,0)
        return res

# if total + num > target:
#                     break  # 排序后后面数字更大，直接剪枝
def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []
        candidates.sort()
        def backtrack(start, total):
            if total == target:
                res.append(path.copy())
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if total + num > target:
                    break  # 排序后后面数字更大，直接剪枝
                path.append(num)
                backtrack(i, total + num)
                path.pop()
        backtrack(0, 0)
        return res

"""
77给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
"""
def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        path = []
        def backtrack(startidx):
            if len(path) == k:
                res.append(path.copy())
                return
            
            for i in range(startidx, n+1):
                path.append(i)
                backtrack(i+1)
                path.pop()
        backtrack(1)
        return res