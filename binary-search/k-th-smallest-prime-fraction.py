from operator import itemgetter
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # [1,2,3,5]
        # [1,7,11,13]
        # 1/13, 1/11, 1/7, 7/13, 7/11, 11/13
        # 3 fractions to consider that are divided by 5
        # 2 fractions to consider that are divided by 3
        # 1 fraction to consider that is divided by 2
        length_arr = len(arr)
        results_list = []
        for i in range(length_arr - 1):
            for j in range(i + 1, length_arr):
                results_list.append((arr[i], arr[j], arr[i]/arr[j]))
        
        results_list.sort(key=itemgetter(2))
        #print(results_list)
        return [results_list[k - 1][0], results_list[k - 1][1]]