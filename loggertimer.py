import time


def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        end = time.time()
        total = end-start
        print("Time To Run : ", total)
        return rv

    return wrapper


def logger(func):

    def wrapper(*args, **kwargs):
        print("Beginning of {} \n\n\n".format(func.__name__))
        rv = func()
        print("\n\n\nEnd of {}".format(func.__name__))
        return rv

    return wrapper


@timer
@logger
def test():
    print("testing")


test()
