class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        num_indices = len(indices)
        answer = [0] * num_indices
        i = 0
        for index in indices:
            answer[index] = s[i]
            i += 1
        return ''.join(answer)