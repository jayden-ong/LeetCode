class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Want to determine all palindromic strings in s
        length_s = len(s)
        palindromic_strings = set()
        for i in range(1, length_s + 1):
            for j in range(length_s - i + 1):
                curr_string = s[j:j + i]
                if curr_string == curr_string[::-1]:
                    palindromic_strings.add(curr_string)
        
        def determine_palindromic(curr_string):
            length_curr_string = len(curr_string)

            if length_curr_string == 0:
                return [[]]
            elif length_curr_string == 1:
                return [[curr_string]]

            answer = []
            for i in range(1, length_curr_string + 1):
                first_partition = curr_string[:i]
                if first_partition in palindromic_strings:
                    curr_results = determine_palindromic(curr_string[i:])
                    for result in curr_results:
                        result.insert(0, first_partition)
                        answer.append(result)
            return answer


        return determine_palindromic(s)

        

            
