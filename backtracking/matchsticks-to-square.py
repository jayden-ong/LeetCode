class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        target = total_length // 4
        matchsticks.sort(reverse=True)
        def choice(curr_index, length1, length2, length3, length4):
            if curr_index >= len(matchsticks):
                if [length1, length2, length3, length4] == [target] * 4:
                    return True
                return False
            
            if length1 > target or length2 > target or length3 > target or length4 > target:
                return False
            
            answer = False
            if length1 + matchsticks[curr_index] <= target:
                answer = answer or choice(curr_index + 1, length1 + matchsticks[curr_index], length2, length3, length4)
            
            if not answer and length2 + matchsticks[curr_index] <= target:
                answer = answer or choice(curr_index + 1, length1, length2 + matchsticks[curr_index], length3, length4)
            
            if not answer and length3 + matchsticks[curr_index] <= target:
                answer = answer or choice(curr_index + 1, length1, length2, length3 + matchsticks[curr_index], length4)
            
            if not answer and length4 + matchsticks[curr_index] <= target:
                answer = answer or choice(curr_index + 1, length1, length2, length3, length4 + matchsticks[curr_index])
            return answer

        return choice(0, 0, 0, 0, 0)