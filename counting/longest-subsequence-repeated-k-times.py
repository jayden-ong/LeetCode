class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def determine_valid_subsequence(subsequence):
            curr_sub_index = 0
            num_appear = 0
            for char in s:
                if char == subsequence[curr_sub_index]:
                    curr_sub_index += 1
                    if curr_sub_index == len(subsequence):
                        num_appear += 1
                        curr_sub_index = 0
            
            return num_appear >= k
        
        answer = ""
        queue = deque()
        queue.append("")
        while queue:
            # Search through all possible characters
            curr_string = queue.popleft()
            if len(curr_string) > 7:
                continue
            for additive in range(26):
                curr_char = chr(ord('a') + additive)
                # Want to see if we can add more characters to it
                if determine_valid_subsequence(curr_string + curr_char):
                    answer = curr_string + curr_char
                    queue.append(curr_string + curr_char)
        return answer