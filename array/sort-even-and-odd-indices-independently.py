class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_indices = []
        odd_indices = []
        num_even = 0
        num_odd = 0
        num_nums = len(nums)
        for i in range(num_nums):
            if i % 2 == 0:
                even_indices.append(nums[i])
                num_even += 1
            else:
                odd_indices.append(nums[i])
                num_odd += 1
        
        even_indices.sort()
        odd_indices.sort(reverse=True)
        answer = []
        even_index = 0
        odd_index = 0
        while even_index < num_even and odd_index < num_odd:
            answer.append(even_indices[even_index])
            even_index += 1
            answer.append(odd_indices[odd_index])
            odd_index += 1
        
        if even_index < num_even:
            answer.append(even_indices[even_index])
        return answer