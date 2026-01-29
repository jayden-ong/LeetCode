class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.bookings)):
            booking_start, booking_end = self.bookings[i]
            if end <= booking_start:
                self.bookings.insert(i, (start, end))
                return True
            elif booking_start <= start < booking_end or booking_start < end < booking_end or (start < booking_start and end > booking_start):
                return False
        self.bookings.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)