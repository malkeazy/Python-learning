from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        ind = 0
        while ind < len(nums):
            if ind < len(nums)-1:
                if nums[ind] == nums[ind+1]:
                    count += 1
                    nums.remove(nums[ind])
                else:
                    ind += 1
            else:
                break
        return count

sol = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expected_nums = [0, 1, 2, 3, 4]

k = sol.removeDuplicates(nums)

assert k == len(expected_nums)
for i in range(k):
    assert nums[i] == expected_nums[i]

print("Все проверки пройдены! k =", k)
