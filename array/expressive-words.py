class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        answer = 0
        for word in words:
            i = 0
            j = 0
            valid = True
            while i < len(word) and j < len(s):
                if word[i] != s[j]:
                    valid = False
                    break
                
                curr_letter = word[i]
                num_letter_word = 0
                num_letter_s = 0
                while i < len(word) and word[i] == curr_letter:
                    num_letter_word += 1
                    i += 1
                
                while j < len(s) and s[j] == curr_letter:
                    num_letter_s += 1
                    j += 1
                
                if (num_letter_word == num_letter_s or num_letter_s >= 3) and num_letter_s >= num_letter_word:
                    continue
                else:
                    valid = False
                    break
            if i == len(word) and j == len(s) and valid:
                answer += 1
        return answer
        