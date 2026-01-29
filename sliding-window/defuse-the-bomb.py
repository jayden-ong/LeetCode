class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length_code = len(code)
        if k == 0:
            return length_code * [0]
        elif k > 0:
            # Will always subtract current number
            i = 0
            elements_added = 0
            curr_sum = 0
            answer = []
            while elements_added < k:
                if i + 1 >= length_code:
                    i = 0
                else:
                    i += 1
                curr_sum += code[i]
                elements_added += 1
            
            for j in range(length_code):
                answer.append(curr_sum)
                if i + 1 >= length_code:
                    i = 0
                else:
                    i += 1
                curr_sum += code[i]

                if j != length_code - 1:
                    curr_sum -= code[j + 1]
                
            return answer
        else:
            k *= -1
            curr_sum = 0
            answer = []
            for i in range(length_code - 1, length_code - k - 1, -1):
                curr_sum += code[i]
            print(i)
            for j in range(length_code):
                answer.append(curr_sum)
                curr_sum += code[j]
                curr_sum -= code[i]
                if i >= length_code - 1:
                    i = 0
                else:
                    i += 1
                
            return answer