class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        str_n = str(n)
        def create_configs(digits_dict, digits_required, curr, all_combinations):
            if len(curr) == digits_required:
                all_combinations.append(int(curr))
                return
            
            for digit in digits_dict:
                if digits_dict[digit] > 0:
                    digits_dict[digit] -= 1
                    old = curr
                    curr += str(digit)
                    create_configs(digits_dict, digits_required, curr, all_combinations)
                    digits_dict[digit] += 1
                    curr = old

        # 1 Digit
        #   1
        # 2 Digits
        #   22
        # 3 Digits
        #   1,2,2
        #   3,3,3
        # 4 Digits
        #   1,3,3,3
        #   4,4,4,4
        # 5 Digits
        #   1,4,4,4,4
        #   2,2,3,3,3
        #   5,5,5,5,5
        # 6 Digits
        #   1,2,2,3,3,3
        #   1,5,5,5,5,5
        #   2,2,4,4,4,4
        #   6,6,6,6,6,6
        # 7 Digits
        #   1,2,2,4,4,4,4 
        if len(str_n) == 1:
            if n == 0:
                return 1
            return 22
        elif len(str_n) == 2:
            if 1 <= n < 22:
                return 22
            return 122
        elif len(str_n) == 3:
            if 100 <= n < 122:
                return 122
            elif 122 <= n < 212:
                return 212
            elif 212 <= n < 221:
                return 221
            elif 221 <= n < 333:
                return 333
            return 1333
        elif len(str_n) == 4:
            if 1000 <= n < 1333:
                return 1333
            elif 1333 <= n < 3133:
                return 3133
            elif 3133 <= n < 3313:
                return 3313
            elif 3313 <= n < 3331:
                return 3331
            elif 3331 <= n < 4444:
                return 4444
            return 14444
        elif len(str_n) == 5:
            if n >= 55555:
                return 122333
            # Want to create all possible configs of beautiful numbers with 5 digits
            all_digits = {2 : 2, 3 : 3}
            all_combinations = [14444, 41444, 44144, 44414, 44441, 55555]
            create_configs(all_digits, 5, "", all_combinations)
            all_combinations.sort()
            for combination in all_combinations:
                if n < combination:
                    return combination
        else:
            if n >= 666666:
                return 1224444
            # Want to create all possible configs of beautiful numbers with 5 digits
            all_digits = {2 : 2, 4 : 4}
            all_combinations = [155555, 515555, 551555, 555155, 555515, 555551, 666666]
            create_configs(all_digits, 6, "", all_combinations)
            all_digits = {1 : 1, 2 : 2, 3 : 3}
            create_configs(all_digits, 6, "", all_combinations)
            all_combinations.sort()
            for combination in all_combinations:
                if n < combination:
                    return combination
        # 0 must never appear in the solution
        # 1 000 000 is the largest number
        #   1 224 444 is the largest beautiful number
        
        