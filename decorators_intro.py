# Decorators intro----->
# Decorators : enhance the functionality of other functions.
# @  Use for decorators. syntetic sugar.

def decorators_func(any_function):
    def wrapper_func():
        print("this is awesome function : ")
        any_function()
    return wrapper_func    

@decorators_func # shortcut of functionality enhance
def func1():
    print("this is function one :")
func1()    


@decorators_func
def func2():
    print("this is function two :")    


func2()


#var = decorators_func(func1)
#var()
