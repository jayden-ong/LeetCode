class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        
        def get_perm(num):
            answer = 0
            for i in range(1, num):
                answer += i
            return answer
        
        nums_products = defaultdict(int)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                nums_products[nums[i] * nums[j]] += 1
        
        answer = 0
        for num in nums_products:
            if nums_products[num] > 1:
                answer += get_perm(nums_products[num]) * 8
        return answer