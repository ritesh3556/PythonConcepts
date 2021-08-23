# define greatest------>

a,b,c=map(int,input("enter three number for checking which is greater : ").split())




def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c
big=greatest(a,b,c)
print(f"{big} is greatest ") 