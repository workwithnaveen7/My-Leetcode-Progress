# Last updated: 4/11/2025, 10:06:32 PM
class MyCalendarThree:

    def __init__(self):
        self.timeline=defaultdict(int)
        self.max_overlap=0

    def book(self, start: int, end: int) -> int:
        self.timeline[start]+=1
        self.timeline[end]-=1
        ongoing =0
        for time in sorted(self.timeline):
            ongoing +=self.timeline[time]
            self.max_overlap=max(self.max_overlap, ongoing)
        return self.max_overlap
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)