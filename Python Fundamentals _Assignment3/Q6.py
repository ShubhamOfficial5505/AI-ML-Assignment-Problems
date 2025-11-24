words = ["apple", "banana", "kiwi", "cherry", "mango"]

words_dict = {}

for word in words:
    words_dict.update({ word: len(word) })

print(words_dict)