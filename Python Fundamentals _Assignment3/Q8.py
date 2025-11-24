list1 = input("Enter list1: ").split()
for i in range(0, len(list1)):
    list1[i] = int(list1[i])

list2 = input("Enter list2: ").split()
for j in range(0, len(list2)):
    list2[j] = int(list2[j])

s1 = set(list1)
s2 = set(list2)
if(s1.intersection(s2) == set()):
    print("Given lists have no common elements")
else:
    print("Given lists have common elements")