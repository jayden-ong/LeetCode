class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        left = 1
        right = max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            streak = 0
            bouquets = 0
            for flower in bloomDay:
                if mid >= flower:
                    streak += 1
                    if streak >= k:
                        bouquets += 1
                        streak = 0
                else:
                    streak = 0
                    
            if bouquets >= m:
                right = mid - 1
            else:
                left = mid + 1
        return left
    