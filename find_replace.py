#replace()
string="he is good and he is best"
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","was",1))



#find()
is_pos1=string.find("is")
print(string.find("is",1))

print(string.find("is",is_pos1 + 1)) 