# *args as argument--------->
def mul_nums(*num): # Noromal variable can't write after *args 
    mul = 1
    print(type(num))
    for i in num:
        mul *= i
    return mul
nu = [1,2,3]    
print(mul_nums(*nu))    