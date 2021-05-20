
import time


def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        end = time.time()
        total = end-start
        print("\n\n\nTime To Run : ", total)
        return rv

    return wrapper


@timer
def test():
    time.sleep(1.5)


test()
