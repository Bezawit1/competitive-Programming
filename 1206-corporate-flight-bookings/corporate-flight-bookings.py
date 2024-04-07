class Solution(object):
    def corpFlightBookings(self, bookings, n):
        answer = [0] * (n + 1)
        prefix_sum = [0] * (n + 1)
        for first, last, reserved in bookings:
            answer[first - 1] += reserved
            answer[last] -= reserved

        
        prefix_sum[0] = answer[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + answer[i]

        prefix_sum.pop()

        return prefix_sum
        