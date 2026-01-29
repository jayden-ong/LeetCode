class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year1, month1, day1 = date1.split("-")
        month_dict = {"01" : 0, "02" : 31, "03" : 59, "04" : 90, "05" : 120, "06" : 151, "07" : 181, "08" : 212, "09" : 243, "10" : 273, "11" : 304, "12" : 334}
        month_leap_dict = {"01" : 0, "02" : 31, "03" : 60, "04" : 91, "05" : 121, "06" : 152, "07" : 182, "08" : 213, "09" : 244, "10" : 274, "11" : 305, "12" : 335}
        
        years1_since = int(year1) - 1971
        num_leap1 = years1_since // 4
        if years1_since % 4 >= 2:
            num_leap1 += 1
        
        if (int(year1) % 4 == 0 and int(year1) % 100 != 0) or int(year1) % 400 == 0:
            date1_day = month_leap_dict[month1] + int(day1) + (num_leap1 * 366) + ((years1_since - num_leap1) * 365)
        else:
            date1_day = month_dict[month1] + int(day1) + (num_leap1 * 366) + ((years1_since - num_leap1) * 365)
        
        year2, month2, day2 = date2.split("-")
        years2_since = int(year2) - 1971
        num_leap2 = years2_since // 4
        if years2_since % 4 >= 2:
            num_leap2 += 1
        
        if (int(year2) % 4 == 0 and int(year2) % 100 != 0) or int(year2) % 400 == 0:
            date2_day = month_leap_dict[month2] + int(day2) + (num_leap2 * 366) + ((years2_since - num_leap2) * 365)
        else:
            date2_day = month_dict[month2] + int(day2) + (num_leap2 * 366) + ((years2_since - num_leap2) * 365)
        return max(date1_day - date2_day, date2_day - date1_day)