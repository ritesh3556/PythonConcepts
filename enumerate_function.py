names = ['abc','abcde','ritesh']

for i in range(len(names)):
    print(f"{i} -----> {names[i]}")

# Position track by enumerate function------>


for pos,i in enumerate(names):
    print(f"{pos} ------> {i}")

def f(l,s):
    for pos,i in enumerate(l):
        if (i == s):
            return pos
    return -1
names = ['abc','abcde','ritesh']    
print(f(names,'abcde'))        





