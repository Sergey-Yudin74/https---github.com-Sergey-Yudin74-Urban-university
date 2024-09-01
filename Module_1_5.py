immutable_var = 1, 2, 3, "Urban"
tuple_= immutable_var
print(tuple_)
#tuple_ [0]= 20 "Кортеж не поддерживает обращение по элементам. Кортеж является неизменяемым 'архивом'. При этом, кортеж может соддержать внутри себя изменяемые элементы."
print(tuple_)
mutable_list = ['X', 'Y', 'Z', 'G']
mutable_list[0] = "A"
print(mutable_list)
print(type(mutable_list))