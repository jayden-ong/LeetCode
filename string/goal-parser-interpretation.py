class Solution:
    def interpret(self, command: str) -> str:
        length_command = len(command)
        i = 0
        answer = ""
        while i < length_command:
            if command[i] == "G":
                answer += "G"
                i += 1
            elif command[i] == "(":
                if command[i + 1] == ")":
                    answer += "o"
                    i += 2
                else:
                    answer += "al"
                    i += 4
        return answer