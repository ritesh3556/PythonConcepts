# Advance min() and max()-------->




students = {
    'harshit' : {'score' : 90, 'age' : 24},
    'mohit' : {'score' : 75, 'age' : 19},
    'rohit' : {'score' : 76, 'age' : 23}
}

student2 = [
    {'name':'harshit' ,'score' : 90, 'age' : 24},
    {'name' : 'mohit' , 'score' : 75, 'age' : 19},
    {'name' : 'rohit' , 'score' : 76, 'age' : 23}
]
print(max(student2,key = lambda items: items.get('score')))
print(max(students, key = lambda items: students[items]['score']))