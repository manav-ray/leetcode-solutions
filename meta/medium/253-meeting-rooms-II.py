"""

Line sweep algorithm
*We DON'T need to keep track of pairs*

 - Essentially, want to go through meetings in ascending order and figure out when a room is needed, and when a room frees up.
 - Start times add a room and end times free up a room
    - Use an array and add all start and end times to it
    - Sort this array so we have all the events in ascending order. This helps with the line sweep
- Keep track of active rooms by += 1 for start times and -= 1 for end times. Each iteration, update res to be the max active rooms

Time complexity - O(nlogn)
Space complexity - O(n)


"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 0
        events = []

        for i in intervals:
            start, end = i
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort()
        activeRooms = 0

        for e in events:
            activeRooms += e[1]
            res = max(res, activeRooms)


        return res