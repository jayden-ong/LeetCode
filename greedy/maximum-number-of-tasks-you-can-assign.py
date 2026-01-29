class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        answer = 0
        worker_index = 0
        def check(num_tasks):
            sidelined = deque()
            worker_index = len(workers) - 1
            num_pills = pills

            for task in reversed(tasks[:num_tasks]):
                if sidelined and sidelined[0] >= task:
                    sidelined.popleft()
                elif worker_index >= 0 and workers[worker_index] >= task:
                    worker_index -= 1
                else:
                    if num_pills == 0:
                        return False
                    
                    while worker_index >= 0 and workers[worker_index] + strength >= task:
                        sidelined.append(workers[worker_index])
                        worker_index -= 1
                    
                    if not sidelined:
                        return False
                    sidelined.pop()
                    num_pills -= 1
            return True

        left, right = 0, min(len(tasks), len(workers))
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return max(0, left - 1)