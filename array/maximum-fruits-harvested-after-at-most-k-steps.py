class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # You only want to reverse direction once
        # Start with the fruit at the furthest left
        #    We can determine which fruits we can reach by storing the positions of fruits to the right
        fruits_left = []
        start_left = -1
        num_fruits_left = 0
        fruits_right = []
        start_right = -1
        num_fruits_right = 0
        base = 0
        for i, (pos, num_fruits) in enumerate(fruits):
            if pos < startPos:
                if abs(pos - startPos) <= k:
                    heapq.heappush(fruits_left, (-pos, num_fruits))
                    if start_left == -1:
                        start_left = i
                    num_fruits_left += num_fruits
            elif pos == startPos:
                base = num_fruits
            else:
                if abs(pos - startPos) <= k:
                    heapq.heappush(fruits_right, (pos, num_fruits))
                    start_right = max(start_right, i)
                    num_fruits_right += num_fruits
        # print(num_fruits_left)
        # print(num_fruits_right)

        answer = max(num_fruits_left, num_fruits_right) + base
        if start_left == -1:
            start_left = 0
        
        if start_right == -1:
            start_right = len(fruits) - 1
        
        curr_fruits = num_fruits_left + base
        for i in range(start_left, len(fruits)):
            pos, num_fruits = fruits[i]
            steps_leftover = k - (startPos - pos)
            if not fruits_right or pos >= startPos:
                break

            while fruits_right and fruits_right[0][0] - pos <= steps_leftover:
                curr_fruits += heapq.heappop(fruits_right)[1]
            
            answer = max(curr_fruits, answer)
            curr_fruits -= num_fruits
            
        
        curr_fruits = num_fruits_right + base
        for i in range(start_right, -1, -1):
            pos, num_fruits = fruits[i]
            steps_leftover = k - (pos - startPos)
            # print(steps_leftover)
            if not fruits_left or pos <= startPos:
                break
            
            while fruits_left and pos - abs(fruits_left[0][0]) <= steps_leftover:
                curr_fruits += heapq.heappop(fruits_left)[1]
            
            answer = max(curr_fruits, answer)
            # print(curr_fruits)
            curr_fruits -= num_fruits
        return answer