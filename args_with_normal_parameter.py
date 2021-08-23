# *args with normal parameter--------->

def mul_nums(num,*args): # Noromal variable can't write after *args 
    mul = 1
    print(type(args))
    print(num)
    print(args)
    for i in args:
        mul *= i
    return mul
print(mul_nums(2,4,3,4))    