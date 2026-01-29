class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month <= 2:
            month += 12
            year -= 1
        
        year_of_century = year % 100
        century = year // 100
        decade = month

        weekday = (day + (13 * (decade + 1) // 5) + year_of_century + (year_of_century // 4) + (century // 4) - (2 * century)) % 7

        weekday_dict = {1 : "Sunday", 2 : "Monday", 3 : "Tuesday", 4 : "Wednesday", 5 : "Thursday", 6 : "Friday", 0 : "Saturday"}
        return weekday_dict[weekday]
