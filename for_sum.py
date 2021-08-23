sum=0
n = int(input("enter any number sum ujpto that\n"))
for i in range(1,n+1):
   print(f"{i}")
   sum+=i
print(f"sum is = {sum}")  

sum=0
n=input("enter any number \n")
for i in range(0,len(n)):
    sum+=int(n[i])
print(sum)        

name = input("enter any name for counting\n")
temp_var = ""    
for i in range(0,len(name)):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")    