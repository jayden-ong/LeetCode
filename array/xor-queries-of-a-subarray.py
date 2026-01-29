class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        curr_left = 0
        curr_right = 0
        dp_left = []
        dp_right = []
        for i in range(len(arr)):
            curr_left ^= arr[i]
            dp_left.append(curr_left)
            curr_right ^= arr[len(arr) - i - 1]
            dp_right.append(curr_right)
        dp_right = dp_right[::-1]
        final = curr_left
        
        answer = []
        for left, right in queries:
            temp = final
            if left > 0:
                temp ^= dp_left[left - 1]
            
            if right < len(arr) - 1:
                temp ^= dp_right[right + 1]
            answer.append(temp)
        return answer 