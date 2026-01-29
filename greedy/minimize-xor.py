class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        binary_string1 = format(num1, 'b')
        binary_string2 = format(num2, 'b')
        num_set = 0
        for bit in binary_string2:
            if bit == '1':
                num_set += 1
        
        if num_set > len(binary_string1):
            return int(num_set * '1', 2)
        
        answer = ""
        for i in range(len(binary_string1)):
            if len(binary_string1) - i == num_set:
                return int((answer + ('1' * (len(binary_string1) - i))), 2)
            
            if num_set == 0:
                return int((answer + ('0' * (len(binary_string1) - i))), 2)
            
            if binary_string1[i] == '0':
                answer += '0'
            else:
                answer += '1'
                num_set -= 1
        
        if num_set > 0:
            answer = (num_set * '1') + answer
        return int(answer, 2)