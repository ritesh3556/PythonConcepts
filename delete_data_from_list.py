# delete data from list-------->



# pop method
fruits1 = ["mango","orange","banana","grapes"]
print(fruits1.pop())
print(fruits1)



# delete operator------>
fruits1 = ["mango","orange","banana","grapes"]

del fruits1[1]
print(fruits1)

# remove method ----> like we dont know the particular location of element in the list and wants to remove the we use remove method.
fruits1.remove("banana")
print(fruits1)
fruits1 = ["mango","mango","orange","banana","grapes"]
fruits1.remove("mango")
print(fruits1)

# data add----->
#1-append
#2-extend
#3-insert

#delete ----->
#pop
#del
#remove