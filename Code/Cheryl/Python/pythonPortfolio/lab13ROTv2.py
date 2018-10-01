#lab 13 ROT version 2
import string

alphabet = 'abcdefghijklmnopqrstuvwxyz '
rot =      'nopqrstuvwxyzabcdefghijklm '
user_info = input('Please enter a phrase. >  ')
rotation = int(input('Please enter the amount of rotation you would like the encryption to use. >  '))
output_string = []
new_var = string.ascii_lowercase[rotation:] + string.ascii_lowercase[:rotation]



if rotation >= 1:
    for character in user_info:
        index = new_var.find(character)
        output_string.append(rot[index])

else:
    for character in user_info:
        index = alphabet.find(character)
        output_string.append(rot[index])


print(''.join(output_string))

