import time


class Timer:
    def __init__(self, limit_seconds):
        self.limit_seconds = limit_seconds
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.start_time = None

    def elapsed_seconds(self):
        assert self.start_time, "Timer must be started first"

        current = time.time()
        return current - self.start_time

    def has_expired(self):
        return self.elapsed_seconds() > self.limit_seconds
