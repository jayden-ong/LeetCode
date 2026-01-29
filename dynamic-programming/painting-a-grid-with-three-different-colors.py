class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # If you add a column, multiply the answer for n - 1 columns by 2
        # 2 * 2 - 30
        # 5 * 1 - 48
        MOD = pow(10, 9) + 7

        # We can enumerate all combinations of red, green, blue using pow(3, m) since that's how many combinations there are
        valid_colours = {}
        for i in range(pow(3, m)):
            curr = []
            curr_val = i
            for j in range(m):
                curr.append(curr_val % 3)
                curr_val //= 3
            
            is_valid = True
            for j in range(m - 1):
                if curr[j] == curr[j + 1]:
                    is_valid = False
                    break
            
            if is_valid:
                valid_colours[i] = curr
        
        # Want to figure out which columns can go one after the other
        valid_adjacent = defaultdict(list)
        for column1, colour1 in valid_colours.items():
            for column2, colour2 in valid_colours.items():
                is_valid = True
                for i in range(m):
                    if colour1[i] == colour2[i]:
                        is_valid = False
                        break
                if is_valid:
                    valid_adjacent[column1].append(column2)
        
        # Want to create a list where list[colour1] is the amount of valid combinations ending in colour1
        dp = []
        for i in range(pow(3, m)):
            if i in valid_colours:
                dp.append(1)
            else:
                dp.append(0)
        
        for i in range(1, n):
            curr = [0] * pow(3, m)
            for column1 in valid_colours.keys():
                # This tells us how many valid combinations there are that end with each possible type of column
                for column2 in valid_adjacent[column1]:
                    curr[column1] += dp[column2]
                    if curr[column1] >= MOD:
                        curr[column1] -= MOD
            
            dp = curr
        return sum(dp) % MOD