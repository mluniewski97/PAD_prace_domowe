phone = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
{'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, 
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# sorting by color
print (sorted(phone, key = lambda i: i['color']))
# sorting by model
print (sorted(phone, key = lambda i: i['model']))
# sorting by make
print (sorted(phone, key = lambda i: i['make']))
