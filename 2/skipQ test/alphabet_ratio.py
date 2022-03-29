import re

mystr = 'This is my STR. It contains some text. And I\'m supposed to check their percentage'


mystr_upper = mystr.upper()
str_cleaned = re.sub(r'[^a-zA-Z\d:]', '', mystr_upper)
unique_characters = list(set(str_cleaned))


occurances = dict()

for character in unique_characters:
    occurances[character] = mystr.upper().count(character)

total_char = len(str_cleaned)
print('Total characters: ', total_char)
for char, occu in occurances.items():
    print(f'{char}: {occu}/{total_char} = {occu/total_char}%')
