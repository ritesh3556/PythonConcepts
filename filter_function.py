def is_even(a):
    return a%2 == 0
numbers = [3,4,2,1,5,6,9,8,10]
evens = list(filter(lambda a:a%2 == 0,numbers))
print(evens)

evens = tuple(filter(lambda a:a%2 == 0,numbers))
for i in evens:
    print(i)
for i in evens:
    print(i)    

print([i for i in numbers if i%2 == 0])    