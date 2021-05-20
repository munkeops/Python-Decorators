
def logger(func):

    def wrapper(*args,**kwargs):
        print("Beginning of {} \n\n\n".format(func.__name__))
        rv=func()
        print("\n\n\nEnd of {}".format(func.__name__))
        return rv

    return wrapper
        
@logger
def test():
    print("testing")

test()