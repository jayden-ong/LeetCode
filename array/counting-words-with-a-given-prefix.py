class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0
        length_pref = len(pref)
        for word in words:
            if word[:length_pref] == pref:
                answer += 1
        return answer