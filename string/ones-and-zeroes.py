class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs_dict = {}
        for string in strs:
            if string not in strs_dict:
                strs_dict[string] = [string.count("0"), string.count("1")]
        
        dp = {}
        def choice(num_zeros, num_ones, curr_index):
            if curr_index >= len(strs):
                return 0

            if curr_index in dp and (num_zeros, num_ones) in dp[curr_index]:
                return dp[curr_index][(num_zeros, num_ones)]
            
            curr_string = strs[curr_index]
            answer = 0
            if num_zeros + strs_dict[curr_string][0] <= m and num_ones + strs_dict[curr_string][1] <= n:
                answer = max(answer, choice(num_zeros + strs_dict[curr_string][0], num_ones + strs_dict[curr_string][1], curr_index + 1) + 1)
            answer = max(answer, choice(num_zeros, num_ones, curr_index + 1))

            if curr_index not in dp:
                dp[curr_index] = {}
            
            if (num_zeros, num_ones) not in dp[curr_index]:
                dp[curr_index][(num_zeros, num_ones)] = answer
            else:
                dp[curr_index][(num_zeros, num_ones)] = max(answer, dp[curr_index][(num_zeros, num_ones)])
            
            return answer
        
        return choice(0, 0, 0)