class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        num_logs = len(logs)
        answer = logs[0][0]
        longest_time = logs[0][1]
        for i in range(1, num_logs):
            if logs[i][1] - logs[i - 1][1] > longest_time or (logs[i][1] - logs[i - 1][1] == longest_time and logs[i][0] < answer):
                answer = logs[i][0]
                longest_time = logs[i][1] - logs[i - 1][1]
        return answer