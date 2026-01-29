class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 0
        right = position[-1] - position[0]
        answer = 0
        
        while left <= right:
            mid = (left + right) // 2
            prev_pos = position[0]
            curr_balls = 1
            for i in range(1, len(position)):
                if position[i] - prev_pos >= mid:
                    curr_balls += 1
                    prev_pos = position[i]
            
            if curr_balls >= m:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer