class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        strings_set = set()
        answer = 0
        for word in words:
            if word[::-1] in strings_set:
                answer += 1
                strings_set.remove(word[::-1])
            else:
                strings_set.add(word)
        return answer