class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # What class will be bossted the most by adding the extra student
        classes_heap = []
        for num_pass, total_students in classes:
            # Want to determine how much of a boost the average would get
            boost = ((num_pass + 1) / (total_students + 1)) - (num_pass / total_students)
            heapq.heappush(classes_heap, (-boost, num_pass, total_students))
        
        for i in range(extraStudents):
            curr_boost, num_pass, total_students = heapq.heappop(classes_heap)
            curr_boost *= -1
            num_pass += 1
            total_students += 1
            new_boost = ((num_pass + 1) / (total_students + 1)) - (num_pass / total_students)
            heapq.heappush(classes_heap, (-new_boost, num_pass, total_students))
        
        answer = 0
        while classes_heap:
            _, num_pass, total_students = heapq.heappop(classes_heap)
            answer += num_pass / total_students
        return answer / len(classes)