class Solution:
    def digitCount(self, num: str) -> bool:
        num_dict = {}
        length_num = 0
        for char in num:
            if char in num_dict:
                num_dict[char] += 1
            else:
                num_dict[char] = 1
            length_num += 1
        
        for i in range(length_num):
            if (str(i) in num_dict and num_dict[str(i)] == int(num[i])) or (str(i) not in num_dict and int(num[i]) == 0):
                continue
            else:
                return False
        return True