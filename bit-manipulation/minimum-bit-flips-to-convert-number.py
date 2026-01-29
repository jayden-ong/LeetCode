class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        binary_start = format(start, "b")
        binary_end = format(goal, "b")

        length_start = len(binary_start)
        length_end = len(binary_end)
        i = length_start - 1
        j = length_end - 1
        answer = 0
        while i > -1 or j > -1:
            if i == -1:
                if binary_end[j] == "1":
                    answer += 1
                j -= 1
            elif j == -1:
                if binary_start[i] == "1":
                    answer += 1
                i -= 1
            else: 
                if binary_start[i] != binary_end[j]:
                    answer += 1
                i -= 1
                j -= 1
        return answer