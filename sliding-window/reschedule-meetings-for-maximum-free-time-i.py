class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # end is EXCLUSIVE
        def get_total_length(start, end):
            answer = 0
            for i in range(start, end):
                answer += endTime[i] - startTime[i]
            return answer
        
        if k >= len(startTime):
            return eventTime - get_total_length(0, len(startTime))
        # Try moving consecutive groups of k
        answer = 0
        for i in range(len(startTime) - k + 1):
            if i == 0:
                lower_bound = 0
            else:
                lower_bound = endTime[i - 1]
            
            if i == len(startTime) - k:
                upper_bound = eventTime
            else:
                upper_bound = startTime[i + k]
            
            if i == 0:
                total_length = get_total_length(i, i + k)
            else:
                total_length += (endTime[i + k - 1] - startTime[i + k - 1])
            answer = max(answer, upper_bound - lower_bound - total_length)
            total_length = total_length - (endTime[i] - startTime[i])
        return answer
