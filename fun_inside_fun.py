# function inside function----->
# define greatest------>

a,b,c=map(int,input("enter three number for checking which is greater : ").split())




def greater(a,b):
    if a > b:
        return a
    return b
def greatest(a,b,c) :
    return greater(greater(a,b),c)
print(f"{greatest(a,b,c)} is bigger")   

