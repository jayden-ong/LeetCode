from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges_dict = defaultdict(set)
        in_degree = defaultdict(int)
        courses_to_prereq = defaultdict(set)
        for prereq, course in prerequisites:
            edges_dict[prereq].add(course)
            in_degree[course] += 1
        
        courses_queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                courses_queue.append(i)
        
        while courses_queue:
            curr_course = courses_queue.popleft()
            # Need to investigate all courses it is a prereq of
            for course in edges_dict[curr_course]:
                in_degree[course] -= 1
                courses_to_prereq[course].add(curr_course)
                for prereq in courses_to_prereq[curr_course]:
                    courses_to_prereq[course].add(prereq)
                
                # Only add if all prior connections have been explored
                if in_degree[course] == 0:
                    courses_queue.append(course)
        
        answer = []
        for prereq, course in queries:
            if prereq in courses_to_prereq[course]:
                answer.append(True)
            else:
                answer.append(False)
        return answer
                