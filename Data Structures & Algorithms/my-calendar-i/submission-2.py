import heapq
class MyCalendar:
    
    def __init__(self):
        self.calendar = []
        heapq.heapify(self.calendar)

    def book(self, startTime: int, endTime: int) -> bool:
        if self.calendar:
            cal_copy = list(self.calendar)
            while cal_copy:
                s, e = heapq.heappop(cal_copy)
                if startTime < e and s < endTime:
                    return False
                else:
                    continue
            
            if len(cal_copy) == 0:
                heapq.heappush(self.calendar, (startTime, endTime))
                return True
        else:
            heapq.heappush(self.calendar, (startTime, endTime))
            return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)