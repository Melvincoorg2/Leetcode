class MyCalendarTwo:

    def __init__(self):
        self.singles = []
        self.doubles = []

    def book(self, startTime: int, endTime: int) -> bool:
        # check against double bookings first
        for s, e in self.doubles:
            if startTime < e and endTime > s:   # overlap → triple booking
                return False

        # find overlaps with singles → becomes double booked
        for s, e in self.singles:
            if startTime < e and endTime > s:
                self.doubles.append((max(startTime, s), min(endTime, e)))

        self.singles.append((startTime, endTime))
        return True    


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)