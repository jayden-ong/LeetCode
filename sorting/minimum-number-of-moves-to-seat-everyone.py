class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        answer = 0
        num_students = len(students)
        for i in range(num_students):
            answer += abs(students[i] - seats[i])
        return answer