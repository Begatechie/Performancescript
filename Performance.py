#import the time module
from time import time

#create a decorator that calculates the time taken to perform a function
def performance(fn):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result =fn(*args, **kwargs)
        t2 = time()
        print (f'it took {t2-t1} seconds to run this function')
        return result
    return wrap_func

#calling the decorator on any function
@performance
def function():
    for x in range(1000000):
        x*5
        
function()
