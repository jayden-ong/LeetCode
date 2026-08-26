class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # calculate length of shortest beautiful substring
        ones_queue = deque()
        smallest_length = len(s) + 1
        for i, char in enumerate(s):
            if char == '1':
                ones_queue.append(i)
            
            if len(ones_queue) == k:
                smallest_length = min(smallest_length, ones_queue[-1] - ones_queue[0] + 1)
                ones_queue.popleft()
        
        if smallest_length == len(s) + 1:
            return ""
        
        # Find lexicographically smallest string using sliding window
        num_ones = 0
        for i in range(smallest_length):
            if s[i] == '1':
                num_ones += 1
        
        answer = ""
        for i in range(len(s) - smallest_length + 1):
            if num_ones == k:
                if answer == "":
                    answer = s[i:i + smallest_length]
                else:
                    answer = min(answer, s[i:i + smallest_length])
            
            if s[i] == '1':
                num_ones -= 1
            
            if i + smallest_length < len(s) and s[i + smallest_length] == '1':
                num_ones += 1
        return answer