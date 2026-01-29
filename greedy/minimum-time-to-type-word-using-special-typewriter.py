class Solution:
    def minTimeToType(self, word: str) -> int:
        curr_pos = "a"
        answer = 0
        for char in word:
            if char == curr_pos:
                answer += 1
            else:
                if char > curr_pos:
                    answer += min(ord(char) - ord(curr_pos), 26 - (ord(char) - ord(curr_pos)))
                else:
                    answer += min(ord(curr_pos) - ord(char), 26 - (ord(curr_pos) - ord(char)))
                answer += 1
                curr_pos = char
        return answer