class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        nums_count = [0] * (max(nums) + 1)
        for num in nums:
            nums_count[num] += 1
        
        for i in range(1, max(nums) + 1):
            for j in range(i * 2, max(nums) + 1, i):
                nums_count[i] += nums_count[j]
        
        for i in range(1, max(nums) + 1):
            nums_count[i] = nums_count[i] * (nums_count[i] - 1) // 2
        
        for i in range(max(nums), 0, -1):
            for j in range(i * 2, max(nums) + 1, i):
                nums_count[i] -= nums_count[j]
        
        for i in range(1, max(nums) + 1):
            nums_count[i] += nums_count[i - 1]
        
        answer = []
        for query in queries:
            query += 1
            answer.append(bisect_left(nums_count, query))
        return answer
 