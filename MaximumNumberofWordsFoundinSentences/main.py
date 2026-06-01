from typing import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        length = 0
        for sentence in sentences:
            lengthSentence = len(sentence.split())
            if lengthSentence > length:
                length = lengthSentence
        return length
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
solution = Solution()
print(solution.mostWordsFound(sentences))