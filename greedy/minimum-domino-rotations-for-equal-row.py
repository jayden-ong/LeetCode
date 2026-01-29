class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        nums_dict = defaultdict(list)
        required = len(tops)
        satisfied = False
        answer = None
        num_same = 0
        for i in range(len(tops)):
            if nums_dict[tops[i]] == []:
                nums_dict[tops[i]] = [1, 0, 1]
            else:
                nums_dict[tops[i]][0] += 1
                nums_dict[tops[i]][2] += 1
            
            if nums_dict[bottoms[i]] == []:
                nums_dict[bottoms[i]] = [0, 1, 1]
            else:
                nums_dict[bottoms[i]][1] += 1
                nums_dict[bottoms[i]][2] += 1
            
            if tops[i] == bottoms[i]:
                nums_dict[bottoms[i]][2] -= 1
            
            if bottoms[i] == tops[i]:
                num_same += 1
            
            if nums_dict[tops[i]][2] == required or nums_dict[bottoms[i]][2] == required:
                satisfied = True
                if nums_dict[tops[i]][2] == required:
                    answer = tops[i]
                else:
                    answer = bottoms[i]
        
        if not satisfied:
            return -1
        return min(nums_dict[answer][0], nums_dict[answer][1]) - num_same