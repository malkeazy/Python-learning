from typing import List
class Solution:
    def countDigits(self, num: int) -> int:
        nextNum, count = num, 0
        while nextNum > 0:
            if nextNum % 10 != 0 and num % (nextNum % 10) == 0:
                count += 1
            nextNum //= 10
        return count
num = 1248
solution = Solution()
print(solution.countDigits(num))


