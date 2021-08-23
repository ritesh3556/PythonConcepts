# nested list------>
example = [[1,2,3],[1,2,3],[1,2,3]]
new_list = [[i for i in range(1,4)] for j in range(3)]
print(new_list)
n = int(input("enter"))
x =[]
for i in range(n):
    ui = int(input())
    x.append(ui)
print(x)    
