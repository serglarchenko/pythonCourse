import time


class Timer:
    def __init__(self, wait_desc):
        self.wait_desc = wait_desc

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f'timer: block {self.wait_desc} executed in {round(self.end_time - self.start_time, 3)} sec')


# with Timer('doing some sleeps'):
#     time.sleep(1)
#     time.sleep(2)
#     time.sleep(3)
