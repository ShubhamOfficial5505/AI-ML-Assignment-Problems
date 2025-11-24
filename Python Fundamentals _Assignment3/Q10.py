string = input("Enter string: ")

char_count = {}

for ch in string:
    if(char_count.get(ch) == None):
        char_count.update({ ch: 1 })
    else:
        char_count[ch] += 1

print("Unique Characters: ", end = "")
unique_ch_count = 0
for ch, count in char_count.items():
    if (count == 1):
        print(ch, end = " ")
        unique_ch_count += 1

print(f"\nCount = { unique_ch_count }")