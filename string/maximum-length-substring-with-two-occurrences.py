class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # sliding window strategy
        first_char_index = 0
        curr_letters_dict = {}
        answer = 0
        curr = 0
        for i in range(len(s)):
            if s[i] in curr_letters_dict:
                curr_letters_dict[s[i]] += 1
            else:
                curr_letters_dict[s[i]] = 1
            
            if curr_letters_dict[s[i]] > 2:
                curr_letters_dict[s[first_char_index]] -= 1
                first_char_index += 1
                while curr_letters_dict[s[i]] > 2:
                    curr_letters_dict[s[first_char_index]] -= 1
                    first_char_index += 1
                    curr -= 1
            else:
                curr += 1
            answer = max(answer, curr)
        return max(answer, curr)
