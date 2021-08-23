# Intro to generators---->

# generators are iterators----->


print("GENERATORS ")
# generators function


def nums(a):
    for i in range(1,a+1):
        yield i
     
n=nums(10)
for num in n:
    print(num)
for num in n:
    print(num)   
    
           




