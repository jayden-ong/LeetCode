class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0
        
        words_length = len(words)
        prev_index = (startIndex - 1 + words_length) % words_length
        next_index = (startIndex + 1) % words_length
        curr_distance = 1
        while words[prev_index] != words[startIndex] or words[next_index] != words[startIndex]:
            if words[prev_index] == target or words[next_index] == target:
                return curr_distance
            prev_index = (prev_index - 1 + words_length) % words_length
            next_index = (next_index + 1) % words_length
            curr_distance += 1
        return -1