class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        curr_cand = []
        curr_degree = 0
        num_to_remove = 0
        nums_dict = {}
        num_nums = 0
        for num in nums:
            num_nums += 1
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
            
            if nums_dict[num] > curr_degree:
                curr_degree = nums_dict[num]
                curr_cand = [num]
                num_to_remove = 1
            elif nums_dict[num] == curr_degree:
                curr_cand.append(num)
                num_to_remove += 1
        
        # Want to gather the first occurrences of each candidate from left and right
        left = 0
        right = num_nums - 1
        places_dict = {}
        best_score = float('inf')
        for cand in curr_cand:
            places_dict[cand] = [-1, -1]
        
        while left < num_nums and right > -1:
            #print(places_dict)
            if nums[left] in places_dict and places_dict[nums[left]][0] == -1:
                places_dict[nums[left]][0] = left
                if places_dict[nums[left]][0] != -1 and places_dict[nums[left]][1] != -1:
                    best_score = min(best_score, places_dict[nums[left]][1] - places_dict[nums[left]][0] + 1)
            #print(places_dict)
            if nums[right] in places_dict and places_dict[nums[right]][1] == -1:
                places_dict[nums[right]][1] = right
                if places_dict[nums[right]][0] != -1 and places_dict[nums[right]][1] != -1:
                    best_score = min(best_score, places_dict[nums[right]][1] - places_dict[nums[right]][0] + 1)
            left += 1
            right -= 1
        return best_score
                