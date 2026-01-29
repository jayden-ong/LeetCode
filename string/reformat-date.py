class Solution:
    def reformatDate(self, date: str) -> str:
        # Get the day number from the string
        date_list = date.split(" ")
        curr_day = ""
        for char in date_list[0]:
            if not char.isnumeric():
                break
            else:
                curr_day += char
        
        # Add 0 if less than 10
        if int(curr_day) < 10:
            curr_day = "0" + curr_day
        
        month_dict = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}
        curr_month = month_dict[date_list[1]]
        # Year doesn't need to be altered
        return date_list[2] + "-" + curr_month + "-" + curr_day