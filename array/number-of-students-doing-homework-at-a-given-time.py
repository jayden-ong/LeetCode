class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        num_students = len(startTime)
        answer = 0
        for i in range(num_students):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                answer += 1
        return answer