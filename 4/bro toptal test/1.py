from math import ceil


class Solution:
    def solution(self, X, B, Z):
        if Z < 1 or len(B) < 1 or X < 1:
            return -1

        try:
            total_B_downloaded = sum(B)

            if total_B_downloaded >= X:
                return 0

            minutes_to_avg = min(len(B), Z)
            avg_time_per_byte = sum(B[-1:-minutes_to_avg-1:-1]) / minutes_to_avg

            remaining_B = X - total_B_downloaded
            remaining_time = ceil(remaining_B / avg_time_per_byte)
        
            return remaining_time
        except:
            return -1


print(Solution().solution(100, [10, 6, 6, 8], 2))
