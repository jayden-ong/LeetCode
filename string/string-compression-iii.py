class Solution:
    def compressedString(self, word: str) -> str:
        curr_char = word[0]
        curr_count = 1
        answer = ""
        for i in range(1, len(word)):
            char = word[i]
            if curr_char != char or curr_count >= 9:
                answer += str(curr_count) + curr_char
                curr_char = char
                curr_count = 1
            else:
                curr_count += 1
        
        answer += str(curr_count) + curr_char
        return answer

