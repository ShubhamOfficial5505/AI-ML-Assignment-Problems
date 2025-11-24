# Input list1
list1 = input("Enter 1st list: ").split()
for i in range(0, len(list1)):
    list1[i] = int(list1[i])

# Input list2
list2 = input("Enter 2nd list: ").split()
for j in range(0, len(list2)):
    list2[j] = int(list2[j])

# Merging into one list
result = []

for integers in list1:
    result.append(integers)

for integers in list2:
    result.append(integers)

# Sorting
result.sort()

print(result)