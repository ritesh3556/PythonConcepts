# any() and all() function--------->


number1 = [2,4,6,8,10,11]
number2 = [1,2,3,4,5,6]


even = []
for i in number1:
    even.append(i%2==0)

print(even)    


print(all([True, True, True, True, True])) #---->

# practice----->





#print(all([i%2==0 for i in number1 ]))


#print(all([True, True, True, True, True])) #---->



#print(any([i%2==0 for i in number1 ]))


def check(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        t = 0
        for num in args:
            t += num
        return t


print(check(1,2,3,4,5,8300362))          
