class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        curr, curr_count = s[0], 1
        starting = curr
        answer = 0
        blocks = [1]
        for i in range(1, len(s)):
            char = s[i]
            if curr == '1':
                answer = max(answer, curr_count)
            if char == curr:
                curr_count += 1
            else:
                blocks.append(curr_count)
                curr = char
                curr_count = 1
        
        blocks.append(curr_count)
        blocks.append(1)

        if len(blocks) <= 4:
            if starting == '0':
                if len(blocks) == 3:
                    return 0
                return blocks[2]
            return blocks[1]
        
        actual_start = 2
        if starting == '1':
            actual_start = 3
        
        for i in range(actual_start, len(blocks) - 2, 2):
            curr_answer = 0
            if i - 2 > 0:
                curr_answer += blocks[i - 2]
            
            if i + 2 < len(blocks) - 1:
                curr_answer += blocks[i - 2]
            curr_answer += blocks[i - 1] + blocks[i] + blocks[i + 1]
            answer = max(answer, curr_answer)
        return answer