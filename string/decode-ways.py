class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        answer = 0
        valid = set()
        for i in range(1, 27):
            valid.add(str(i))
        
        def choice(curr_index, curr_string):
            answer = 0
            if curr_index >= len(s):
                if curr_string in valid:
                    return 1
                return 0
            
            if s[curr_index] == '0' and curr_string == "":
                return 0
            
            # Can choose to add next character to current string -- only if the curr_string is valid
            if curr_string + s[curr_index] in valid:
                answer += choice(curr_index + 1, curr_string + s[curr_index])

            # Can choose to complete letter and make index part of current string
            if curr_string in valid:
                answer += choice(curr_index + 1, s[curr_index])
            
            return answer

        if s[0] in valid:
            answer += choice(1, s[0])
        
        return answer
        '''

        dp = []
        if s[0] == "0":
            return 0
        
        dp.append(1)
        dp.append(1)
        for i in range(2, len(s) + 1):
            curr_val = 0
            if s[i - 2] != '0' and ((int(s[i - 2]) < 2) or (int(s[i - 2]) == 2 and int(s[i - 1]) <= 6)):
                curr_val += dp[i - 2]
            
            if s[i - 1] != '0':
                curr_val += dp[i - 1]
            dp.append(curr_val)
        return dp[-1]