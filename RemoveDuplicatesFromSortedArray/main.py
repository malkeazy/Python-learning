from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for ind in range(len(nums)):
            if nums[slow] != nums[ind]:
                slow += 1
                nums[slow] = nums[ind]
        return slow + 1

sol = Solution()
nums = [7, 7, 7]
print(sol.removeDuplicates(nums))
expected_nums = [7]

k = sol.removeDuplicates(nums)

assert k == len(expected_nums)
for i in range(k):
    assert nums[i] == expected_nums[i]

print("Все проверки пройдены! k =", k)
