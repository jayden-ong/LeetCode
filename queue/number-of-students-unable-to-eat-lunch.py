class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_sandwiches = len(sandwiches)
        sandwich_index = 0

        # Students count list
        students_count = [0, 0]
        for student in students:
            students_count[student] += 1

        if students_count[1] == sum(sandwiches):
            return 0
        
        while sandwich_index != num_sandwiches:
            curr_sandwich = sandwiches[sandwich_index]
            # Move student to end of queue
            if students_count[curr_sandwich] == 0:
                return students_count[1 - curr_sandwich]
            students_count[curr_sandwich] -= 1
            sandwich_index += 1

        return 0
