class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Split expression into numbers and signs
        expression_list = []
        curr = ""
        for char in expression:
            if char in "*+-":
                expression_list.append(int(curr))
                expression_list.append(char)
                curr = ""
            else:
                curr += char
        
        if curr != "":
            expression_list.append(int(curr))

        # Want to store all possibilities we have seen so far
        answer_dict = {}
        def compute_possibilities(expression_list):
            # Base case
            if len(expression_list) == 1:
                return [expression_list[0]]
            
            if tuple(expression_list) in answer_dict:
                return answer_dict[tuple(expression_list)]
            
            # If the base case does not happen, there must be at least one more number and sign
            # Cannot have something like [1, '*']
            answer = []
            
            # We then have to take the next part of the expression and get all possibilities
            for i in range(1, len(expression_list), 2):
                first_part = compute_possibilities(expression_list[:i])
                second_part = compute_possibilities(expression_list[i + 1:])
                # expression_list[i] is our operation
                for first_num in first_part:
                    for second_num in second_part:
                        if expression_list[i] == "+":
                            answer.append(first_num + second_num)
                        elif expression_list[i] == "-":
                            answer.append(first_num - second_num)
                        else:
                            answer.append(first_num * second_num)
            answer_dict[tuple(expression_list)] = answer
            return answer
        
        return compute_possibilities(expression_list)