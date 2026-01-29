class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if k > len(colors):
            return 0
        
        is_alternating = []
        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                is_alternating.append(True)
            else:
                is_alternating.append(False)
        
        if colors[0] != colors[-1]:
            is_alternating.append(True)
        else:
            is_alternating.append(False)
        
        num_true = 0
        num_false = 0
        for i in range(k - 1):
            if is_alternating[i]:
                num_true += 1
            else:
                num_false += 1
        
        answer = 0
        for i in range(len(colors)):
            if num_true == k - 1:
                answer += 1
            
            if is_alternating[i]:
                num_true -= 1
            else:
                num_false -= 1

            if is_alternating[(i + k - 1) % len(colors)]:
                num_true += 1
            else:
                num_false += 1
        return answer