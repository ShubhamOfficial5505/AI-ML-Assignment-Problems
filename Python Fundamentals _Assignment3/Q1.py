string = input("Enter String: ")

palindrome = True

s_idx = 0
e_idx = len(string) - 1
while(s_idx < e_idx):
    if(string[s_idx] != string[e_idx]):
        palindrome = False
        break
    
    s_idx += 1
    e_idx -= 1

if(palindrome == True):
    print(f"{ string } is palindrome")
else:
    print(f"{ string } is not palindrome")