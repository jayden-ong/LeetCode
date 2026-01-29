class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        answer = []
        for i in range(len(code)):
            curr_code, curr_business, curr_active = code[i], businessLine[i], isActive[i]
            if len(curr_code) == 0:
                continue
            
            if curr_business not in ["electronics", "grocery", "pharmacy", "restaurant"]:
                continue
            
            if not curr_active:
                continue
            
            valid = True
            for char in curr_code:
                if 48 <= ord(char) <= 57:
                    continue
                elif 65 <= ord(char) <= 90:
                    continue
                elif 97 <= ord(char) <= 122:
                    continue
                elif ord(char) == 95:
                    continue

                valid = False
                break

            if not valid:
                continue

            answer.append((curr_business, curr_code))
        answer = sorted(answer, key=lambda x:(x[0], x[1]))
        final = []
        for curr_code in answer:
            final.append(curr_code[1])
        return final