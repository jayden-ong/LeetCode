class Solution:
    def isHappy(self, n: int) -> bool:
        nums_collected = []
        curr_num = n
        while True:
            curr_val = 0
            curr_num_str = str(curr_num)
            for i in range(len(curr_num_str)):
                curr_val += int(curr_num_str[i]) ** 2
                
            if curr_val == 1:
                return True
            
            if curr_val in nums_collected:
                return False
            nums_collected.append(curr_val)
            curr_num = curr_val
