from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Want to find the two numbers arr[l] <= x <= arr[r]
        for i in range(len(arr) + 1):
            if i == 0:
                if x < arr[i]:
                    l = -1
                    r = 0
                    break
            elif i == len(arr):
                if x >= arr[i - 1]:
                    l = i - 1
                    r = len(arr)
                    break
            else:
                if arr[i - 1] <= x <= arr[i]:
                    l = i - 1
                    r = i
                    break
        
        answer = deque()
        while len(answer) != k:
            if l > -1 and (r == len(arr) or abs(arr[l] - x) <= abs(arr[r] - x)):
                answer.appendleft(arr[l])
                l -= 1
            else:
                answer.append(arr[r])
                r += 1
        return answer