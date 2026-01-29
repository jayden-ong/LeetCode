from collections import deque
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # There are k - 1 sequences to check in each window
        valid_sequence = deque()
        num_true = 0
        # Develop initial subarray
        answer = []
        if k == 1:
            valid_sequence.append(True)
            num_true += 1
            answer.append(nums[0])
        else:
            for i in range(k - 1):
                if nums[i + 1] == nums[i] + 1:
                    num_true += 1
                    valid_sequence.append(True)
                else:
                    valid_sequence.append(False)
        
            if num_true == k - 1:
                answer.append(nums[k - 1])
            else:
                answer.append(-1)
        
        for i in range(k, len(nums)):
            # Remove first element of subarray because window is moving
            if valid_sequence[0]:
                num_true -= 1
            valid_sequence.popleft()
            
            if (k > 1 and nums[i] == nums[i - 1] + 1) or k == 1:
                num_true += 1
                valid_sequence.append(True)
            else:
                valid_sequence.append(False)
            
            if num_true == k - 1 or k == 1:
                answer.append(nums[i])
            else:
                answer.append(-1)
        return answer
