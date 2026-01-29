class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        answer_array = [0] * n
        answer_array[0] = 1
        i = 1
        curr_index = 0
        while True:
            new_holder = curr_index + (i * k)
            new_holder %= n
            answer_array[new_holder] += 1
            if answer_array[new_holder] == 2:
                break
            curr_index = new_holder
            i += 1
        
        answer = []
        for i in range(n):
            if answer_array[i] == 0:
                answer.append(i + 1)
        return answer