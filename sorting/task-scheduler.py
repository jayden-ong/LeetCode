class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_dict = {}
        for task in tasks:
            if task in tasks_dict:
                tasks_dict[task] += 1
            else:
                tasks_dict[task] = 1
        
        total_jobs = 0
        most_freq = 0
        num_most_freq = 0
        for key in tasks_dict:
            total_jobs += tasks_dict[key]
            if tasks_dict[key] > most_freq:
                most_freq = tasks_dict[key]
                num_most_freq = 1
            elif tasks_dict[key] == most_freq:
                num_most_freq += 1
        return max(total_jobs, (most_freq - 1) * (n + 1) + num_most_freq)