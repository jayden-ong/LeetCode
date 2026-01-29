class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bit_dict = {0 : -1}
        curr_mask = 0
        answer = 0
        i = 0
        for letter in s:
            if letter == 'a':
                curr_mask ^= 16
            elif letter == 'e':
                curr_mask ^= 8
            elif letter == 'i':
                curr_mask ^= 4
            elif letter == 'o':
                curr_mask ^= 2
            elif letter == 'u':
                curr_mask ^= 1
            
            if curr_mask in bit_dict:
                answer = max(answer, i - bit_dict[curr_mask])
            else:
                bit_dict[curr_mask] = i
            i += 1
        return answer
