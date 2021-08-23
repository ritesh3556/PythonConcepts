# decorators with argument--------->
from functools import wraps
def only_data_types(data_types):
    def decorators(functions):
        @wraps(functions)
        def wrapper(*args,**kwargs):
            if all([type(arg)==data_types for arg in args]):
                return functions(*args,**kwargs)
        return wrapper
    `return decorators


@only_data_types(str)
def string_join(*args):
    s=''
    for i in args:
        s+=i
    return s
print(string_join('harshit','vashitha','a'))    