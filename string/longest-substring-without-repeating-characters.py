class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub = 0
        curr_sub = 0
        char_dict = {}
        char_queue = []
        for char in s:
            # Found a new character that is not already in the substring
            if char_dict.get(char, 0) == 0:
                curr_sub += 1
                char_dict[char] = 1
                char_queue.append(char)
            else:
                longest_sub = max(longest_sub, curr_sub)
                # Want to find the first instance of the repeated character and remove it
                while char_queue and char_queue[0] != char:
                    char_dict[char_queue.pop(0)] -= 1
                    curr_sub -= 1
                # Once we find the repeated instance, remove it
                # Char should be in queue according to dict
                char_queue.pop(0)
                char_queue.append(char)
        
        return max(longest_sub, curr_sub)