"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
"""
def solution283(self, nums: list[int]) -> None:
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
"""
def removeElement1(self, nums: list[int], val: int) -> int:
        res = []
        for num in nums:
            if num != val:
                res.append(num)
        # 把res的元素写回nums原地,`nums[:] = res` 是修改原数组内容；如果写 `nums = res` 只是改变局部变量，仍然错误。
        nums[:] = res
        return len(res)


def removeElement2(self, nums: list[int], val: int) -> int:
        slow =0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow +=1
        return slow

def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] !=0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow +=1

"""
给你一个有序数组 nums ，请你 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
"""
def removeDuplicates(self, nums: list[int]) -> int:
        slow = 1
        count = 2

        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow +=1
        return slow 

# 快慢指针的本质是 不断扩大合法区间[0 ... slow-1]，只有当满足条件的时候区间扩大