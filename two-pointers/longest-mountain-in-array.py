class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        answer = 0
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left = i
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                
                right = i
                while right < len(arr) - 1 and arr[right] > arr[right + 1]:
                    right += 1
                
                answer = max(answer, right - left + 1)
        return answer