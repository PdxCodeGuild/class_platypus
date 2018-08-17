abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = input("Enter your message to encrypt. ").upper()
rotation = int(input("what rotation do you want? "))

for char in message:
    index = abc.find(char)
    if index == -1:
        print(char, end='')
    else:
        index += rotation
        index %= 26
        print(abc[index], end='')
