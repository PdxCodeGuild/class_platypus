rot = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}
#extra = ['?', ' ', '.', '!', ',', "'"]

#rotate = input(int('how many rotations for encryption key?'))
input_string = input('what is the word you would like to encrypt? ').lower()
output_string = ''
for letter in input_string:
    if letter in output_string:
        encrypt = rot[letter]
        output_string += encrypt
    else:
        encrypt = rot[letter]
        output_string += encrypt

#if input_string in extra:


print(output_string)





