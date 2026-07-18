from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 0
        while ind < len(nums)-1:
            if nums[ind] == nums[ind+1]:
                del nums[ind]
            else:
                ind += 1
        return len(nums)

sol = Solution()
nums = [0, 0, 1, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6]
expected_nums = [0, 1, 2, 3, 4, 5, 6]

k = sol.removeDuplicates(nums)

assert k == len(expected_nums)
for i in range(k):
    assert nums[i] == expected_nums[i]

print("Все проверки пройдены! k =", k)
