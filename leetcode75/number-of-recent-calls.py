class RecentCounter:
    TIME_RANGE = 3000

    def __init__(self):
        self.ping_timestamps = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.ping_timestamps.append(t)
        while self.ping_timestamps[self.start] < t - self.TIME_RANGE:
            self.start += 1
        return len(self.ping_timestamps) - self.start
