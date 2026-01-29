class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        def gcd(num1, num2):
            while max(num1, num2) % min(num1, num2) > 0:
                num1, num2 = max(num1, num2) % min(num1, num2), min(num1, num2)
            return min(num1, num2)
        available_indices = [0]
        for i in range(len(nums) - 1):
            curr_gcd = gcd(nums[i], nums[i + 1])
            if curr_gcd > 1:
                curr_lcm = nums[i] * nums[i + 1] // curr_gcd
                nums[i], nums[i + 1] = 0, curr_lcm
                
                if available_indices and available_indices[-1] == i:
                    available_indices.pop()
                
                # Go back and check
                while available_indices:
                    curr_gcd = gcd(nums[available_indices[-1]], nums[i + 1])
                    if curr_gcd > 1:
                        curr_lcm = nums[available_indices[-1]] * nums[i + 1] // curr_gcd
                        nums[available_indices[-1]], nums[i + 1] = 0, curr_lcm
                        available_indices.pop()
                    else:
                        break

            if i + 1 < len(nums) - 1:
                available_indices.append(i + 1)
        answer = []
        for num in nums:
            if num != 0:
                answer.append(num)
        return answer