class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for word in words:
            new_word = word.split(separator)
            for subword in new_word:
                if subword != "":
                    answer.append(subword)
        return answer