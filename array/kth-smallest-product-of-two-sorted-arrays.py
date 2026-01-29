class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Want to figure out if the result is negative or positive
        def find_num_neg(nums_list):
            num_neg = 0
            for i in range(len(nums_list)):
                if nums_list[i] < 0:
                    num_neg += 1
                elif nums_list[i] > 0:
                    break
            return num_neg
        
        num_neg_nums1 = find_num_neg(nums1)
        num_neg_nums2 = find_num_neg(nums2)
        left, right = -(10 ** 10), 10 ** 10
        while left <= right:
            mid = (left + right) // 2
            curr = 0
            index_nums1, index_nums2 = 0, num_neg_nums2 - 1
            while index_nums1 < num_neg_nums1 and index_nums2 >= 0:
                if nums1[index_nums1] * nums2[index_nums2] > mid:
                    index_nums1 += 1
                else:
                    curr += num_neg_nums1 - index_nums1
                    index_nums2 -= 1
            
            index_nums1, index_nums2 = num_neg_nums1, len(nums2) - 1
            while index_nums1 < len(nums1) and index_nums2 >= num_neg_nums2:
                if nums1[index_nums1] * nums2[index_nums2] > mid:
                    index_nums2 -= 1
                else:
                    curr += index_nums2 - num_neg_nums2 + 1
                    index_nums1 += 1

            index_nums1, index_nums2 = 0, num_neg_nums2
            while index_nums1 < num_neg_nums1 and index_nums2 < len(nums2):
                if nums1[index_nums1] * nums2[index_nums2] > mid:
                    index_nums2 += 1
                else:
                    curr += len(nums2) - index_nums2
                    index_nums1 += 1
            
            index_nums1, index_nums2 = num_neg_nums1, 0
            while index_nums1 < len(nums1) and index_nums2 < num_neg_nums2:
                if nums1[index_nums1] * nums2[index_nums2] > mid:
                    index_nums1 += 1
                else:
                    curr += len(nums1) - index_nums1
                    index_nums2 += 1
            
            if curr < k:
                left = mid + 1
            else:
                right = mid - 1

        return left
