import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        meet_ct = [0] * n
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        busy_rooms = [] # (end_time, room_id)

        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room)
            
            if available_rooms:
                room = heapq.heappop(available_rooms)
                meet_ct[room] += 1
                heapq.heappush(busy_rooms, (end, room))
            else:
                earliest_end, room = heapq.heappop(busy_rooms)
                meet_ct[room] += 1
                heapq.heappush(busy_rooms, (earliest_end + (end - start), room))
        
        max_meetings = max(meet_ct)
        for i in range(n):
            if meet_ct[i] == max_meetings:
                return i