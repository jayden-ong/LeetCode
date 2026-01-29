class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks_heap = []
        self.tasks_to_prio = {}
        for user, task, prio in tasks:
            heapq.heappush(self.tasks_heap, (-prio, -task, user))
            self.tasks_to_prio[task] = (prio, user)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.tasks_heap, (-priority, -taskId, userId))
        self.tasks_to_prio[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        _, user = self.tasks_to_prio[taskId]
        self.tasks_to_prio[taskId] = (newPriority, user)
        heapq.heappush(self.tasks_heap, (-newPriority, -taskId, user))

    def rmv(self, taskId: int) -> None:
        _, user = self.tasks_to_prio[taskId]
        self.tasks_to_prio[taskId] = (-1, -1)

    def execTop(self) -> int:
        while self.tasks_heap:
            prio, task, user = heapq.heappop(self.tasks_heap)
            prio, task = -prio, -task
            if (prio, user) == self.tasks_to_prio[task]:
                self.tasks_to_prio[task] = (-1, user)
                return user
            
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()