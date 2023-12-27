import time


class Clock:
    def start(self):
        self.start = time.time()

    def stop(self):
        end = time.time()
        return end - self.start
