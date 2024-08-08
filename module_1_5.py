#hw2
immutable_var = 1, 2, 3, False, 'Craft', "Milk"
print(immutable_var)
#hw3
#immutable_var[0] = 2 ,
#print(immutable_var) # выдает ошибку так-как при обращении к кортежу по индексу изменить элементы в кортеже нельзя!
#кортеж — неизменяемый тип данных и что после создания кортежа его элементы невозможно изменить
immutable_var = ([1, 2, 3], [ False ], ['Craft'], ["Milk"])
print(immutable_var)
immutable_var[-1][-1] = 8
print(immutable_var)
immutable_var = ([1, 2, 3], [ False ], ['Craft'], ["Milk"]) * 6
print(immutable_var)
#hw4
mutable_list = [1, 2, 3, False, 'Craft', "Milk"]
print(mutable_list)
mutable_list [2] = 33
print(mutable_list)
mutable_list [0:4] = "look"
print(mutable_list)
mutable_list [0:4] = 'food', 5
mutable_list [3] = True
print(mutable_list)