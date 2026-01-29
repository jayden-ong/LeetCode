class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums_dict = {}
        answer = []
        for num in set(nums1):
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        for num in set(nums2):
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        for num in set(nums3):
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        for num in nums_dict:
            if nums_dict[num] >= 2:
                answer.append(num)
        return answer