class Fenwick:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    
    def update(self, index, delta):
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index
        
    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        reverse = {}
        value_to_index2 = {}
        for i, num in enumerate(nums2):
            value_to_index2[num] = i
        
        for i, num in enumerate(nums1):
            reverse[value_to_index2[num]] = i
        
        tree = Fenwick(len(nums1))
        answer = 0
        for i in range(len(nums1)):
            pos = reverse[i]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (len(nums1) - 1 - pos) - (i - left)
            answer += left * right
        return answer