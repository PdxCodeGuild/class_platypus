# Rot cipher
# Indu thekkemeppilly Sivakumar
# Aug 17 2018
alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = input("Enter the word you want to encrypt\n")
rotation = int(input("whats your desired rotation?"))
converted = ''
for char in text:
    index = alphabet.find(char)
    if index == -1:
        converted += char
    else:
        index += rotation
        if index > len(alphabet):
            index -= len(alphabet)
        converted += alphabet[index]
print(converted)
