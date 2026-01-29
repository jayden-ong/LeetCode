class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        curr_answer = []
        smallest_index_sum = -1

        list1_dict = {}
        num_list1 = len(list1)
        for i in range(num_list1):
            list1_dict[list1[i]] = i
        
        num_list2 = len(list2)
        for i in range(num_list2):
            if list2[i] in list1_dict:
                if smallest_index_sum == -1 or i + list1_dict[list2[i]] < smallest_index_sum:
                    smallest_index_sum = i + list1_dict[list2[i]]
                    curr_answer = [list2[i]]
                elif i + list1_dict[list2[i]] == smallest_index_sum:
                    curr_answer.append(list2[i])
        return curr_answer