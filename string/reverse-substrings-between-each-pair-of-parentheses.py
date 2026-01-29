class Solution:
    def reverseParentheses(self, s: str) -> str:
        curr_string = ""
        stack = []
        for char in s:
            if char == "(":
                stack.append(curr_string)
                curr_string = ""
            elif char == ")":
                string_to_append = stack.pop()
                curr_string = string_to_append + curr_string[::-1]
            else:
                curr_string += char
            print(curr_string)
            print(stack)
        return curr_string