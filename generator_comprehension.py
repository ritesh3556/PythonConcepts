# generator comprehension----->



square = (i**2 for i in range(1,11))
print(next(square))
for s in square:
    print(s)   # printed 
for s in square:
    print(s)    # not printed because use only at once.
    