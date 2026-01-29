class Solution:
    def maximumLength(self, s: str) -> int:
        answer = []
        for i in range(26):
            # First index represents number of occurrences, second contains the three biggest lengths
            answer.append(defaultdict(int))
        
        curr_letter = s[0]
        curr_length = 1
        final_answer = -1
        for i in range(1, len(s) + 1):
            if i < len(s) and s[i] == curr_letter:
                curr_length += 1
            else:
                temp = None
                for j in range(1, curr_length + 1):
                    answer[ord(curr_letter) - 97][j - 1] += (curr_length - j + 1)
                    # It is a possible answer
                    if answer[ord(curr_letter) - 97][j - 1] >= 3:
                        temp = j
                
                if temp is not None:
                    final_answer = max(final_answer, temp)
                
                curr_length = 1
                if i < len(s):
                    curr_letter = s[i]
        return final_answer