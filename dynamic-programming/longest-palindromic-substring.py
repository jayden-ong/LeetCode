class Solution:
    def longestPalindrome(self, s: str) -> str:
        length_s = len(s)
        # Want to store the index of the first character and the current string
        longest = 1
        answer = s[0]
        answers_dict = {}
        for i in range(length_s):
            if i == 0:
                answers_dict[s[i]] = {(0, s[0])}
            elif i == 1:
                if s[i] in answers_dict:
                    answers_dict[s[i]] = {(0, s[:i + 1]), (i, s[i])}
                    longest = 2
                    answer = s[:i + 1]
                else:
                    answers_dict[s[i]] = {(i, s[i])}
            else:
                # If the character is in the dictionary, it can only extend palindromes that begin with s[i]
                if s[i] in answers_dict:
                    curr = set()
                    #print(answers_dict)
                    for palindrome_tuple in answers_dict[s[i]]:
                        starting_index, curr_palindrome = palindrome_tuple
                        # There are no characters in between
                        if i - starting_index - 1 <= 0:
                            curr.add((starting_index, curr_palindrome + s[i]))
                            # Determine curr longest
                            if i - starting_index + 1 > longest:
                                longest = i - starting_index + 1
                                answer = curr_palindrome + s[i]
                        elif (starting_index + 1, s[starting_index + 1:i]) in answers_dict[s[starting_index + 1]]:
                            curr.add((starting_index, s[starting_index:i + 1]))
                            # Determine curr longest
                            if i - starting_index + 1 > longest:
                                longest = i - starting_index + 1
                                answer = s[starting_index:i + 1]
                        else:
                            curr.add((starting_index, s[i]))
                    curr.add((i, s[i]))
                    answers_dict[s[i]] = curr
                # If the character is not in the dictionary, cannot make a palindrome longer
                else:
                    answers_dict[s[i]] = {(i, s[i])}
            #print(s[i])
            #print(answers_dict)
        
        return answer