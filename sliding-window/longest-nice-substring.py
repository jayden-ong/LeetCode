class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        length_s = len(s)
        answer = ""
        answer_length = 0
        for i in range(length_s):
            incomplete_letters = set()
            num_incomplete = 0
            complete_letters = set()
            for j in range(i, length_s):
                if s[j] not in complete_letters:
                    # If it is uppercase, check if its lowercase was already seen
                    if s[j].isupper() and s[j].lower() in incomplete_letters:
                        incomplete_letters.remove(s[j].lower())
                        complete_letters.add(s[j])
                        complete_letters.add(s[j].lower())
                        num_incomplete -= 1
                    elif not s[j].isupper() and s[j].upper() in incomplete_letters:
                        incomplete_letters.remove(s[j].upper())
                        complete_letters.add(s[j])
                        complete_letters.add(s[j].upper())
                        num_incomplete -= 1
                    else:
                        if s[j] not in incomplete_letters:
                            incomplete_letters.add(s[j])
                            num_incomplete += 1
                
                if num_incomplete == 0:
                    if j + 1 - i > answer_length:
                        answer_length = j + 1 - i
                        answer = s[i:j + 1]
        return answer
