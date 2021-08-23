#  function returning two values -------->
def func(int1, int2):
    add = int1 + int2
    multiply = int1 * int2
    return add, multiply

print(func(2,3))
add,multiply = func(2,3)
print(add)
print(multiply)


# range function in tuple---->
nums = tuple(range(1,11))
print(nums)




# tuple change to list----->
#nums = list((1,2,3,4,5,6,7,8,9))
#print(nums)

# its type is str------>
#nums = ((1,2,3,4,5,6,7,8,9))

#numsl = list([1,2,3,4,5,6,7,8,9])
#print(type(numsl))
#n = int(input("enter"))
#num = tuple(range(1,n+1))
#print(sum(num))

#

##
def count_substring(string, sub_string):

    return string.count(sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)