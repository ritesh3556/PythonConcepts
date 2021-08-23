from functools import wraps
def decorators_func(any_function):
    @wraps(any_function)
    def wrapper_func(*args,**kwargs):
        print("this is awesome function : ")
        return any_function(*args,**kwargs)
    return wrapper_func   


@decorators_func
def add(a,b):
    """ this is add function """
    return a + b

print(add(2,8))
print(add.__doc__)
print(add.__name__)