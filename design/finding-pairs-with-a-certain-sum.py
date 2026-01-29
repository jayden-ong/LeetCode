class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_dict = defaultdict(int)
        self.nums1_list = nums1
        for num in nums1:
            self.nums1_dict[num] += 1
        
        self.nums2_dict = defaultdict(int)
        self.nums2_list = nums2
        for num in nums2:
            self.nums2_dict[num] += 1

    def add(self, index: int, val: int) -> None:
        self.nums2_dict[self.nums2_list[index]] -= 1
        self.nums2_dict[self.nums2_list[index] + val] += 1
        self.nums2_list[index] += val

    def count(self, tot: int) -> int:
        answer = 0
        for num in self.nums1_dict:
            if tot - num in self.nums2_dict:
                answer += self.nums2_dict[tot - num] * self.nums1_dict[num]
        return answer
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)