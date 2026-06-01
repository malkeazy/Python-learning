from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate
nums = [5,1,1,5,2,2,2,2,2]
sol = Solution()
print(sol.majorityElement(nums))