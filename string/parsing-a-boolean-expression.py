class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Split an AND or OR expression into sub expressions
        def split_expr(expression):
            answer = []
            i = 0
            while i < len(expression):
                if expression[i] == "t":
                    answer.append("t")
                    i += 1
                elif expression[i] == "f":
                    answer.append("f")
                    i += 1
                else:
                    # We have a NOT, OR, or AND expression
                    curr_expr = expression[i] + "("
                    # Next index has to be an open bracket
                    stack = ["("]
                    i += 2
                    while stack:
                        curr_expr += expression[i]
                        if expression[i] == ")":
                            stack.pop()
                        elif expression[i] == "(":
                            stack.append("(")
                        i += 1
                    answer.append(curr_expr)
                    
                i += 1
            return answer

        def eval_expr(expression):
            if expression == "t":
                return True
            elif expression == "f":
                return False
            elif expression[0] == "!":
                result = eval_expr(expression[2:len(expression) - 1])
                if not result:
                    return True
                else:
                    return False
            else:
                all_expressions = split_expr(expression[2:len(expression) - 1])
                for sub_expression in all_expressions:
                    result = eval_expr(sub_expression)
                    # Don't need to eval anymore
                    if result and expression[0] == "|":
                        return True
                    
                    if not result and expression[0] == "&":
                        return False
                
                if expression[0] == "|":
                    return False
                else:
                    return True
        
        return eval_expr(expression)