class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def get_x_sum(nums_dict):
            heap = []
            for num in nums_dict:
                heapq.heappush(heap, (-nums_dict[num], -num))
            
            num_popped = 0
            answer = 0
            while heap and num_popped < x:
                freq, neg_num = heapq.heappop(heap)
                answer += freq * neg_num
                num_popped += 1
            return answer
        
        nums_dict = defaultdict(int)
        answer = []
        for i in range(k - 1):
            nums_dict[nums[i]] += 1
        
        for i in range(k - 1, len(nums)):
            nums_dict[nums[i]] += 1
            answer.append(get_x_sum(nums_dict))
            nums_dict[nums[i - k + 1]] -= 1
        return answer