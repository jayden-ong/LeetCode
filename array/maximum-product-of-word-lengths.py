class Solution:
    def maxProduct(self, words: List[str]) -> int:
        answer = 0
        for i in range(len(words) - 1):
            word_set = set()
            for char in words[i]:
                word_set.add(char)
            
            for j in range(i + 1, len(words)):
                is_valid = True
                for char in words[j]:
                    if char in word_set:
                        is_valid = False
                        break
                
                if is_valid:
                    answer = max(answer, len(words[i]) * len(words[j]))
        return answer