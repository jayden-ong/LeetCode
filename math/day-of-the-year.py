class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split("-")
        month_dict = {"01" : 0, "02" : 31, "03" : 59, "04" : 90, "05" : 120, "06" : 151, "07" : 181, "08" : 212, "09" : 243, "10" : 273, "11" : 304, "12" : 334}
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
            month_dict = {"01" : 0, "02" : 31, "03" : 60, "04" : 91, "05" : 121, "06" : 152, "07" : 182, "08" : 213, "09" : 244, "10" : 274, "11" : 305, "12" : 335}
        
        return month_dict[month] + int(day)