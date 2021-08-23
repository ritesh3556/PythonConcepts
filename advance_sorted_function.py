# Advance sorted function-------->


guitars = [
      {'model' : 'yamaha f310', 'price' : 8400},
      {'model' : 'faith naptune', 'price' : 50000},
      {'model' : 'faith apollo', 'price': 35000},
      {'model' : 'taylor 814se', 'price' : 450000}

]

print(sorted(guitars,key = lambda items:items['price']))

print(sorted(guitars,key = lambda items:items.get('price')))

print(sorted(guitars,key = lambda items:items['price'],reverse = True