class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nums_dict = {}
        for num in nums:
            new_num = ""
            for char in str(num):
                new_num += str(mapping[int(char)])
            
            if int(new_num) in nums_dict:
                nums_dict[int(new_num)].append(num)
            else:
                nums_dict[int(new_num)] = [num]
                
        nums_heap = []
        for new_num in nums_dict:
            heapq.heappush(nums_heap, (new_num, nums_dict[new_num]))
        
        answer = []
        while nums_heap:
            answer.extend(heapq.heappop(nums_heap)[1])
        return answer