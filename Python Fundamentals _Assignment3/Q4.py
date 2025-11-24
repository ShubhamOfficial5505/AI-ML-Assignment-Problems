tuple_int = (-4, -5, 7, 2, 0, 8, 6, 4)

list_even = []
list_odd = []
for integer in tuple_int:
    if ((integer % 2) == 0):
        list_even.append(integer)
    else:
        list_odd.append(integer)

tuple_even = tuple(list_even)
tuple_odd = tuple(list_odd)

print(tuple_even)
print(tuple_odd)