salary = int(input("Enter Salary: "))

final_tax_rate = None
if (salary < 30000):
    final_tax_rate = 5
elif (salary >= 30000 and salary <= 70000):
    final_tax_rate = 15
else:
    final_tax_rate = 25

print(final_tax_rate)