from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
           if nums[fast] != 0:
               nums[slow], nums[fast] = nums[fast], nums[slow]
               slow += 1



sol = Solution()
nums = [0,0,1,0,3,0,12,0,0]
sol.moveZeroes(nums)
print(nums)