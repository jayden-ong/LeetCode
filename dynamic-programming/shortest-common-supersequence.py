class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = {}
        def get_longest_common_sub(index1, index2):
            # Want to populate dp
            # dp[(i, j)] is the length of the longest common subsequence between first_string[:i], second_string[:j]
            if index1 == -1 or index2 == -1:
                return ("", 0)
            
            # If we have already solved the problem, don't solve again
            if (index1, index2) in dp:
                return dp[(index1, index2)]
            
            answer = 0
            # The optimal solution is to look at the two strings without the last character
            if str1[index1] == str2[index2]:
                temp_string, temp_length = get_longest_common_sub(index1 - 1, index2 - 1)
                answer = (temp_string + str1[index1], 1 + temp_length)
            else:
                first_option = get_longest_common_sub(index1, index2 - 1)
                second_option = get_longest_common_sub(index1 - 1, index2)
                if first_option[1] > second_option[1]:
                    answer = first_option
                else:
                    answer = second_option
            
            dp[(index1, index2)] = answer
            return answer
        
        longest_sub, _ = get_longest_common_sub(len(str1) - 1, len(str2) - 1)
        index1, index2, index3 = 0, 0, 0
        final_answer = ""
        while index1 < len(str1) or index2 < len(str2):
            if index3 < len(longest_sub):
                if str1[index1] == longest_sub[index3] and str2[index2] == longest_sub[index3]:
                    final_answer += str1[index1]
                    index3 += 1
                    index2 += 1
                    index1 += 1
                elif str1[index1] == longest_sub[index3]:
                    final_answer += str2[index2]
                    index2 += 1
                else:
                    final_answer += str1[index1]
                    index1 += 1
            else:
                if index1 < len(str1):
                    final_answer += str1[index1]
                    index1 += 1
                
                if index2 < len(str2):
                    final_answer += str2[index2]
                    index2 += 1

        return final_answer