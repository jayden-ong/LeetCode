from operator import itemgetter
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Want to put the heaviest first
        boxTypes.sort(key=itemgetter(1))
        num_boxes_types = len(boxTypes)
        answer = 0
        for i in range(num_boxes_types - 1, -1, -1):
            if boxTypes[i][0] > truckSize:
                answer += truckSize * boxTypes[i][1]
                return answer
            else:
                answer += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
        return answer