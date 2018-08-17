#lab 13 ROT version 1

alphabet = 'abcdefghijklmnopqrstuvwxyz '
rot =      'nopqrstuvwxyzabcdefghijklm '
user_info = input('Please enter a phrase. >   ')
output_string = []

for character in user_info:
    index = alphabet.find(character)
    output_string.append(rot[index])


print(''.join(output_string))

