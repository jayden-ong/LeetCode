class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        
        # Will set up choice points
        # When we insert first period:
        # -- there must be at most 3 zeros
        # -- there must be at most 9 digits
        def choice(periods_added, curr_ip, leftover):
            if periods_added == 4:
                return [curr_ip[:-1]]
            # At each point, we can add 1, 2 or 3 digits
            answer = []
            # We can add 1 digit
            # Make sure the amount of digits leftover is at most 3 * (4 - periods_added - 1)?
            if len(leftover[1:]) <= 3 * (4 - periods_added - 1) and len(leftover[1:]) >= (4 - periods_added - 1):
                answer += choice(periods_added + 1, curr_ip + leftover[0] + ".", leftover[1:])

            # We can add 2 digits if the first digit is not zero and there are few enough digits remaining
            if leftover[0] != "0" and len(leftover[2:]) <= 3 * (4 - periods_added - 1) and len(leftover[2:]) >= (4 - periods_added - 1):
                answer += choice(periods_added + 1, curr_ip + leftover[:2] + ".", leftover[2:])

            # We can add 3 digits
            if leftover[0] != "0" and len(leftover[3:]) <= 3 * (4 - periods_added - 1) and len(leftover[3:]) >= (4 - periods_added - 1) and int(leftover[:3]) <= 255:
                answer += choice(periods_added + 1, curr_ip + leftover[:3] + ".", leftover[3:])
            return answer

        return list(set(choice(0, "", s)))