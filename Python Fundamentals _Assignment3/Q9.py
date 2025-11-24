given_list = [4, 8, 9, 15, -2, 0, 8, 12, 15, 8]

corresponding_set = set()
multi_appearance_set = set()

for num in given_list:
    if(num in corresponding_set):
        multi_appearance_set.add(num)
    corresponding_set.add(num)

for el in multi_appearance_set:
    print(el)