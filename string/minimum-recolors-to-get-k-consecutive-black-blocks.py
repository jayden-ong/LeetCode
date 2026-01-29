class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        answer = float('inf')
        for i in range(len(blocks) - k + 1):
            curr_config = blocks[i:i + k]
            num_white = curr_config.count("W")
            if num_white == 0:
                return 0
            else:
                answer = min(answer, num_white)
        return answer