class Solution:
    def robotWithString(self, s: str) -> str:
        answer = ""
        leftovers = []
        letters_left = [0] * 26
        for letter in s:
            letters_left[ord(letter) - ord("a")] += 1
        
        curr_index = 0
        for letter in s:
            while letters_left[curr_index] == 0:
                curr_index += 1
            
            # If there is an earlier character later, we need to wait for it
            while leftovers and leftovers[-1] <= chr(curr_index + ord("a")):
                answer += leftovers.pop()
            
            if ord(letter) == curr_index + ord("a"):
                answer += letter
            else:
                leftovers.append(letter)
            letters_left[ord(letter) - ord("a")] -= 1

        leftover_string = ''.join(leftovers)
        return answer + leftover_string[::-1]