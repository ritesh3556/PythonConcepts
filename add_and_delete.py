user_info = {
        'name':'ritesh',
        'age' : 20,
        'class' : 'xyz',
        'fav ' : '5',
        'fav_movies' : ['coco','kimi no na wa']
}


# how to add data --->

user_info['fav_songs'] = ['song1','song2']
print(user_info)


# pop method------->

popped_items = user_info.pop('fav_songs')
print(popped_items)
print(user_info)
print(type(popped_items))


# popitem method------->
popped_item = user_info.popitem()
print(user_info)
print(popped_item)
print(type(popped_item))