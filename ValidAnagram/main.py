class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        symbols = {}
        if len(s) != len(t):
            return False
        for symbol in t:
            symbols[symbol] = symbols.get(symbol, 0) + 1
        for symbol in s:
            if symbol in symbols:
                if symbols[symbol] > 0:
                    symbols[symbol] -= 1
                else:
                    return False
            else:
                return False
        return True
s = "aabb"
t = "aabb"
sol = Solution()
print(sol.isAnagram(s, t))