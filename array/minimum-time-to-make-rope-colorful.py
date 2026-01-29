class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        curr_longest = neededTime[0]
        curr_time = neededTime[0]
        answer = 0
        curr = colors[0]
        for i in range(1, len(neededTime) + 1):
            if i != len(neededTime) and colors[i] == curr:
                curr_time += neededTime[i]
                curr_longest = max(neededTime[i], curr_longest)
            else:
                if curr_time != curr_longest:
                    answer += curr_time - curr_longest
                if i != len(neededTime):
                    curr_longest = neededTime[i]
                    curr_time = curr_longest
                    curr = colors[i]
        return answer