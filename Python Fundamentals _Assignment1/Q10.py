decimal_num = float(input("Enter a Decimal Number: "))

integer_part = int(decimal_num)
fractional_part = decimal_num - int(decimal_num)

print("Integer Part:", integer_part)
print("Fractional Part:", fractional_part)

'''
Some decimal (Base-10) numbers (floats) don't have an exact binary match, so the value is always
slightly approximated during storage. This error is sometimes hidden when the number is displayed
using Python's print function, but it can become apparent during certain operations or comparisons.
'''