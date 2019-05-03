from time import sleep, time
from functools import wraps

def f(sleep_time = 0.1):
    sleep(sleep_time)

def measure(func):
    def wrapper(*args, **args_d):
        t = time()
        func(*args, **args_d)
        print(func.__name__, ' took time:', time()-t)
    return wrapper

f  = measure(f)
#f(1)
#f(sleep_time=1)


def measure(func):
    @wraps(func)
    def wrapper(*args, **args_d):
        t = time()
        func(*args, **args_d)
        print(func.__name__, 'took time:', time()-t)
    return wrapper

@measure
def f(sleep_time=0.2):
    sleep(sleep_time)

#f(2)
print(f.__name__, ':', f.__doc__)

def measure(func):
    @wraps(func)
    def wrapper(*args, **args_d):
        t = time()
        result = func(*args, **args_d)
        print(func.__name__, 'took time:', time()-t)
        return result
    return wrapper

def max_result(func):
    @wraps(func)
    def wrapper(*args, **args_d):
        result = func(*args, **args_d)
        if(result > 100):
            print('Result is too big ({0}). Maximum allowd is 100.'.format(result))
        return result
    return wrapper

@measure
@max_result
def cube(n=1):
    return n**3

#print(cube(2))
#print(cube(5))
#print(cube(2))

def max_result(threshold):
    def decorator(func):
        def wrapper(*args, **args_d):
            result = func(*args, **args_d)
            if( result > threshold):
                print('Result {0} is too big. Maximum allowed is {1}'.format(result, threshold))
            return result
        return wrapper
    return decorator

@max_result(100)
def cube(n):
    return n**3

@max_result(75)
def square(n):
    return n**2

print(cube(5))
print(cube(2))
print(square(5))
print(square(10))

