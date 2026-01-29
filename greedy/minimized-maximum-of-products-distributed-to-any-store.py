class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(k):
            if k == 0:
                return False
            num_places = 0
            new_quantities = []
            for quantity in quantities:
                if quantity > k:
                    new_quantities.append(quantity)
                else:
                    num_places += 1
            
            i = 0
            while num_places <= n and i < len(new_quantities):
                curr_quantity = new_quantities[i]
                # We can perfectly divide the curr_quantity into curr_quantity // k places
                if curr_quantity % k == 0:
                    num_places += curr_quantity // k
                else:
                    num_places += curr_quantity // k + 1
                i += 1

            return i >= len(new_quantities) and num_places <= n
        
        right = sum(quantities)
        left = 0

        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1
        return left