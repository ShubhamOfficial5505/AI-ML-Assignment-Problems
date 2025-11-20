def count_no_of_digits(n):
    count = 0
    while(n != 0):
        count += 1
        n = int(n / 10)
    
    return count

n = int(input("Enter n: "))
print(count_no_of_digits(n))