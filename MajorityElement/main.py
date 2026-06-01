from itertools import count
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
nums = [2,2,31,31,31,1, 1,2,2,2]
sol = Solution()
print(sol.majorityElement(nums))