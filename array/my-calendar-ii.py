class MyCalendarTwo:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        def check_overlap(new_start, new_end):
            num_overlap = 0
            for booking_start, booking_end in self.bookings:
                if new_start < booking_end and new_end > booking_start:
                    num_overlap += 1
                
                if num_overlap >= 2:
                    return True
            return False

        for booking_start, booking_end in self.bookings:
            if start < booking_end and end > booking_start:
                if check_overlap(max(start, booking_start), min(end, booking_end)):
                    return False
        self.bookings.append((start, end))
        return True
                

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)