class Solution:
    def sumZero(self, n: int) -> List[int]:
        num_elements = 0
        curr_element = 1
        answer = []
        while num_elements < n:
            answer.append(curr_element)
            answer.append(curr_element * -1)
            curr_element += 1
            num_elements += 2
        if n % 2 == 1:
            answer = answer[:num_elements - 1]
            answer[-1] = 0
        return answer