my_dict = {
    'x': 10,
    'y': 20,
    'z': 50}
print(my_dict)
print(my_dict['x'])
print(my_dict.get('w', 'Такого ключа нет'))
my_dict.update({
    'w': 170,
    's': 200})
print(my_dict)
#my_dict.pop('x')
print(my_dict)
a = my_dict.pop('x')
print(my_dict)
print(a)
my_set = {1, 1, 3, 3, 5, 4, 4}
my_set = {1, 1, 3, 3, 5, 4, 4, 'Cod', (1, 2, 3)}
list_ = [1, 1, 3, 3, 6, 7, 10, 4, 4]
list_ = set(list_)
print(list_)
print(list_.discard(3))
print(list_)