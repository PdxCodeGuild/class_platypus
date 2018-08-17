english = ['a', 'b', 'c', 'd', 'e', 'f', 'g',  'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Gets the rotation variable from user to make encoded list
rotation = int(input('Enter a number to be used in encyption: '))%26
rotated = english[rotation:] + english[:rotation]
final = ''
entered = input('Enter a string to have it encoded in ROT' + rotation + ': ')
#Loops inputed string and adds the correlating ROT letter to final
for char in entered:
    for slot in range(len(english)):
        if char == english[slot]:
            final = final + rotated[slot]
print(final)
