def decorators_func(any_function):
    def wrapper_func(*args,**kwargs):
        print("this is awesome function : ")
        return any_function(*args,**kwargs)  # return 
    return wrapper_func    

@decorators_func
def func(a):
    print(f"this is function with argument {a}")
func(5)    


@decorators_func
def add(a,b):
    return a + b

print(add(2,8))    