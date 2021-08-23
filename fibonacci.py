num = int(input("enter any number for print fabonacci series upto that\n"))
a=0
b=1
if num == 1:
    print(a)
elif num == 2:
    print(a, b)
else:
    print(a,b, end = " ")
    for i in range(num-2):
        c=a+b
        a=b
        b=c
        print(b,end=" ")            