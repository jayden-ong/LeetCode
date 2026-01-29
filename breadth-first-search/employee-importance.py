from collections import deque
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Want to put all id's into a dict
        employee_dict = {}
        for employee in employees:
            employee_dict[employee.id] = employee
        
        employees_queue = deque()
        employees_queue.append(employee_dict[id])
        answer = 0
        ids_used = set()
        while employees_queue:
            curr_employee = employees_queue.popleft()
            answer += curr_employee.importance
            for employee in curr_employee.subordinates:
                if employee not in ids_used:
                    employees_queue.append(employee_dict[employee])
            ids_used.add(curr_employee.id)

        return answer