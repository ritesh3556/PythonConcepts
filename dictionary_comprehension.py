# dictionary comprehension------->
#square = {1:1,2:4,3:9}
square = {num:num**2 for num in range(1,11)}
print(square)


square = {f"square of {num} is ":num**2 for num in range(1,11)}
print(square)
for k,v in square.items():
    print(f"{k} :{v}")


string = "harshit"
new_dictionary = {char:string.count(char) for char in string}
print(new_dictionary)

