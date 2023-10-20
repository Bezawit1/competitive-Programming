class Solution(object):
    def carPooling(self, trips, capacity):
        passenger = [0] * 1001
    
        for trip in trips:
            pass_count, start, end = trip
            passenger[start] += pass_count
            passenger[end] -= pass_count
        current_passengers = 0
        for count in passenger:
            current_passengers += count
            if current_passengers > capacity:
                return False
        return True








        