import string

# for i in range(26):
#     letters = letters + letters.find(char)
# print(letters)


def rot13(word):

    letters = string.ascii_lowercase
    letters_rot = 'nopqrstuvwxyzabcdefghijklm'
    output = ''

    for chars in letters:
        index = letters.find(chars)
        output += letters_rot[index]

    return output


def rota(word, a):
    letters = string.ascii_lowercase
    output = ''
    for char in word:
        index = letters.find(char)
        index += a

        while index >= len(letters):
                index -= len(letters)
        output += letters[index]

    return output

print(rota('kagomesakura', 13))
