class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        answer = []
        def generate_numbers(curr_number):
            if curr_number > n:
                return
            
            answer.append(curr_number)
            
            for i in range(10):
                new_number = curr_number * 10 + i
                if new_number > n:
                    break
                else:
                    generate_numbers(new_number)
                
            return
        # For every number, if we can get away with adding the next digit, need to consider going 1 to 9
        for i in range(1, 10):
            generate_numbers(i)
        
        return answer