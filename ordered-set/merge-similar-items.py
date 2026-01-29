from operator import itemgetter
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        item_dict = {}
        for item in items1:
            if item[0] in item_dict:
                item_dict[item[0]] += item[1]
            else:
                item_dict[item[0]] = item[1]
        
        for item in items2:
            if item[0] in item_dict:
                item_dict[item[0]] += item[1]
            else:
                item_dict[item[0]] = item[1]
        
        answer = []
        for item in item_dict:
            answer.append([item, item_dict[item]])
        answer.sort(key = operator.itemgetter(0))
        return answer