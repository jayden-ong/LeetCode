class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8 or turnedOn == 0:
            return []
        
        hours_lights = defaultdict(list)
        hours_lights[0].append("0")
        minutes_lights = defaultdict(list)
        minutes_lights[0].append("00")
        if turnedOn > 0:
            hours_lights[1].extend(["1", "2", "4", "8"])
            minutes_lights[1].extend(["01", "02", "04", "08", "16", "32"])
        
        if turnedOn > 1:
            hours_lights[2].extend(["3", "5", "6", "9", "10"])
            minutes_lights[2].extend(["03", "05", "09", "17", "33", "06", "10", "18", "34", "12", "20", "36", "24", "40", "48"])
        
        if turnedOn > 2:
            hours_lights[3].extend(["7", "11"])
            minutes_lights[3].extend(["07", "11", "19", "35", "13", "21", "37", "25", "41", "49", "14", "22", "38", "26", "42", "50", "28", "44", "52", "56"])
        
        if turnedOn > 3:
            minutes_lights[4].extend(["15", "23", "39", "27", "43", "51", "29", "45", "57", "30", "46", "58"]) 
        
        if turnedOn > 4:
            minutes_lights[5].extend(["31", "47", "55", "59"]) 
        
        answer = []
        for i in range(turnedOn + 1):
            for hour in hours_lights[i]:
                for minute in minutes_lights[turnedOn - i]:
                    answer.append(hour + ":" + minute)
        return answer