class Solution:
    def decodeString(self, s: str) -> str:
        # A digit always has to be followed by square brackets
        def recursive_decode(curr_string):
            i = 0
            answer = ""
            while i < len(curr_string):
                if curr_string[i].isdigit():
                    curr_num = ""
                    while curr_string[i].isdigit():
                        curr_num += curr_string[i]
                        i += 1
                    curr_num = int(curr_num)

                    # index i must contain a "["
                    # Will stop once we close square bracket
                    num_open = 1
                    start_index = i
                    i += 1
                    while i < len(curr_string) and num_open != 0:
                        if curr_string[i] == "[":
                            num_open += 1
                        elif curr_string[i] == "]":
                            num_open -= 1
                        i += 1
                    answer += curr_num * recursive_decode(curr_string[start_index + 1:i - 1])
                else:
                    answer += curr_string[i]
                    i += 1

                
            return answer

        return recursive_decode(s)