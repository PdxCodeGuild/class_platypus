# Rot cipher
# Indu thekkemeppilly Sivakumar
# Aug 17 2018
plaintext  = 'abcdefghijklmnopqrstuvwxyz!_@#%^&*()_. '
ciphertext = 'nopqrstuvwxyzabcdefghijklm!_@#%^&*()_. '
character = input("Enter the word you want to encrypt\n")
converted = ''
for char in character:
    index = plaintext.find(char)
    converted += ciphertext[index]
print(converted)
