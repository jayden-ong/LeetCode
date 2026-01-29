class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_time = 0
        num_times = len(timeSeries)
        for i in range(num_times - 1):
            # Time resets
            if timeSeries[i] + duration > timeSeries[i + 1]:
                total_time += timeSeries[i + 1] - timeSeries[i]
            else:
                total_time += duration
        return total_time + duration
