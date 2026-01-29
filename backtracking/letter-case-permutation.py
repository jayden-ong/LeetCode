class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        def create_permutations(curr_index, curr_string):
            if curr_index == len(s):
                answer.append(curr_string)
                return
            
            if s[curr_index].isalpha():
                if s[curr_index].isupper():
                    create_permutations(curr_index + 1, curr_string + s[curr_index].lower())
                else:
                    create_permutations(curr_index + 1, curr_string + s[curr_index].upper())
            
            create_permutations(curr_index + 1, curr_string + s[curr_index])
            return
        
        create_permutations(0, "")
        return answer