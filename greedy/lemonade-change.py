class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_dict = {5 : 0, 10 : 0, 20 : 0}
        for bill in bills:
            if bill == 5:
                change_dict[5] += 1
            elif bill == 10:
                # Need to give back $5 in change
                if change_dict[5] < 1:
                    print(change_dict)
                    return False
                else:
                    change_dict[5] -= 1
                change_dict[10] += 1
            else:
                if change_dict[5] >= 1 and change_dict[10] >= 1:
                    change_dict[5] -= 1
                    change_dict[10] -= 1
                elif change_dict[5] >= 3:
                    change_dict[5] -= 3
                else:
                    print(change_dict)
                    return False
                change_dict[20] += 1
        return True