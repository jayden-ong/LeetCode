class Solution:
    def captureForts(self, forts: List[int]) -> int:
        num_forts = len(forts)
        empty_forts_list = []
        num_command = 0
        num_enemy = 0
        for i in range(num_forts):
            if forts[i] == -1:
                empty_forts_list.append(i)
            elif forts[i] == 1:
                num_command += 1
            elif forts[i] == 0:
                num_enemy += 1
        
        if len(empty_forts_list) == 0 or num_command == 0 or num_enemy == 0:
            return 0
        
        answer = 0
        for empty_fort in empty_forts_list:
            left_index = empty_fort - 1
            left_cap = 0
            right_index = empty_fort + 1
            right_cap = 0
            while left_index > 0  and forts[left_index] == 0:
                left_cap += 1
                left_index -= 1

            while right_index < num_forts - 1 and forts[right_index] == 0:
                right_cap += 1
                right_index += 1
            
            if empty_fort > 0 and forts[left_index] == 1:
                answer = max(answer, left_cap)
            
            if empty_fort < num_forts - 1 and forts[right_index] == 1:
                answer = max(answer, right_cap)
        return answer