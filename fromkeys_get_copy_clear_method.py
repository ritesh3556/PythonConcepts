# fromkeys---->
#d = {'name': 'unknown' , 'age' : 'unknown'}

#d = dict.fromkeys(['name','age','height'],'unknwon')
#print(d)
#d = dict.fromkeys(('name','age','height'),'unknwon')
#print(d)
#d = dict.fromkeys("abc",'unknwon')
#print(d)
#d = dict.fromkeys(range(1,11),'unknwon')
#print(d)
#d = dict.fromkeys(['name','age'],['unknown','unknown'])
#print(d)
d = {'name': 'ritesh' , 'age' : 'unknown'}
print(d['name'])
print(d.get('name'))
print(d.get('names'))


if 'name' in d:
    print('presnt')
else:
    print('not prsent')


# shortcut get method------->


if d.get('name'):
    print('presnt')
else:
    print('not prsnt')

# clear method------->
#d.clear()
print(d)        


d1 = d.copy()


print(d1 is d )

# more about get------>

user = {'name': 'ritesh' , 'age' : 20}
print(user.get('names'))
print(user.get('names', 'notfound'))
user = {'name': 'ritesh' , 'age' : 20,'age' : 34}
print(user)




