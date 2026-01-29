class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # We need to return the minimum amount of indices that have to be deleted
        # Once we hit an index that is wrong, delete it and if the next index is fine, finish
        # 0 = fail, 1 = success, 2 = there is something with the same letter
        def validate(index, unknown, prev_indices):
            same = False
            for i in range(1, len(strs)):
                if strs[i - 1][index] > strs[i][index]:
                    # It is okay if these chars are not in order if the previous ones are
                    if unknown:
                        valid = False
                        for prev_index in prev_indices:
                            # Impossible for strs[i - 1][prev_index] > strs[i][prev_index]
                            # since that would trigger a deletion
                            if strs[i - 1][prev_index] < strs[i][prev_index]:
                                valid = True
                                break

                        if valid:
                            continue
                    return 0
                elif strs[i - 1][index] == strs[i][index]:
                    if unknown:
                        valid = False
                        for prev_index in prev_indices:
                            if strs[i - 1][prev_index] < strs[i][prev_index]:
                                valid = True
                                break

                        if valid:
                            continue
                    same = True
            if same:
                return 2
            return 1
        
        answer = 0
        unknown, prev_indices = False, []
        for i in range(len(strs[0])):
            res = validate(i, unknown, prev_indices)
            if res == 0:
                answer += 1
            elif res == 1:
                return answer
            else:
                unknown = True
                prev_indices.append(i)
            
        return answer