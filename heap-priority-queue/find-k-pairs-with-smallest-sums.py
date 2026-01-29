class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]
        answer = []
        nums_used = set()
        while heap and len(answer) < k:
            _, nums1_index, nums2_index = heapq.heappop(heap)
            answer.append([nums1[nums1_index], nums2[nums2_index]])
            
            if nums1_index < len(nums1) - 1 and (nums1_index + 1, nums2_index) not in nums_used:
                heapq.heappush(heap, (nums1[nums1_index + 1] + nums2[nums2_index], nums1_index + 1, nums2_index))
                nums_used.add((nums1_index + 1, nums2_index))

            if nums2_index < len(nums2) - 1 and (nums1_index, nums2_index + 1) not in nums_used:
                heapq.heappush(heap, (nums1[nums1_index] + nums2[nums2_index + 1], nums1_index, nums2_index + 1))
                nums_used.add((nums1_index, nums2_index + 1))
            
        return answer