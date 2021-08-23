#name="ritesh"
#print(len(name))



def add_two(a,b):
    return a+b
#total=add_two(4,5)    
#$print(total)
#a=int(input("enter first number "))
#b=int(input("enter any second "))
#print(add_two(a,b))
print("Input the value of x & y")
x, y = map(int, input().split())
print(add_two(x,y))


def add_two_string(name1,name2):
    return name1 + name2

f_name = input("enter first name ")
s_name = input("enter second name ")
print(add_two_string(f_name,s_name))    
