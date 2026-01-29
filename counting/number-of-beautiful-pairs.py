class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def is_coprime(num1, num2):
            if num1 == 1 or num2 == 1:
                return True

            smallest = min(num1, num2)
            for i in range(2, smallest + 1):
                if num1 % i == 0 and num2 % i == 0:
                    return False
            
            return True
        
        num_nums = len(nums)
        answer = 0
        for i in range(num_nums - 1):
            for j in range(i + 1, num_nums):
                string_num1 = str(nums[i])
                string_num2 = str(nums[j])
                if is_coprime(int(string_num1[0]), int(string_num2[-1])):
                    answer += 1
        return answer