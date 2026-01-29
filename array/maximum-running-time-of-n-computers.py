class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if len(batteries) < n:
            return 0
        
        # Binary search?
        batteries.sort(reverse=True)
        best_batteries = batteries[:n][::-1]
        extra_power = sum(batteries[n:])
        def validate_time(max_time):
            curr_power = extra_power
            for battery in best_batteries:
                if battery >= max_time:
                    return True
                
                if curr_power < max_time - battery:
                    return False
                curr_power -= (max_time - battery)
            return True
        
        left, right = 0, sum(batteries) // n
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if validate_time(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer