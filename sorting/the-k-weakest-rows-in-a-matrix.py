class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # First index is row, second is num soldiers
        soldiers_dict = {}
        num_rows = len(mat)
        max_soldiers = 0
        for i in range(num_rows):
            num_soldiers = mat[i].count(1)
            max_soldiers = max(num_soldiers, max_soldiers)
            if num_soldiers in soldiers_dict:
                soldiers_dict[num_soldiers].append(i)
            else:
                soldiers_dict[num_soldiers] = [i]
        
        num_elements = 0
        curr_soldiers = 0
        answer = []
        while num_elements < k:
            if curr_soldiers in soldiers_dict:
                answer.extend(soldiers_dict[curr_soldiers])
                soldiers_dict[curr_soldiers].sort()
                num_elements += len(soldiers_dict[curr_soldiers])
            curr_soldiers += 1
        
        return answer[:k]
        