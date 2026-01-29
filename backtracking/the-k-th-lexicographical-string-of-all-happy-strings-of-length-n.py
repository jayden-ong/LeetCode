class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        curr_k = [0]
        answer = []
        def get_happy_string(curr_string):
            if len(curr_string) == n:
                curr_k[0] += 1
                if curr_k[0] == k:
                    answer.append(curr_string)
                    return True
                return False

                return False
            
            for letter in ["a", "b", "c"]:
                if curr_string == "" or curr_string[-1] != letter:
                    if get_happy_string(curr_string + letter):
                        return True
            return False
        
        if get_happy_string(""):
            return answer[0]
        return ""