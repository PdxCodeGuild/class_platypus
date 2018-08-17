english = ['a', 'b', 'c', 'd', 'e', 'f', 'g',  'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rot13 = ['n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c',
         'd', 'e', 'f', 'g',  'h', 'i', 'j', 'k', 'l', 'm']
final = ''
entered = input('Enter a string to have it encoded in ROT13: ')
for char in entered:
    for slot in range(len(english)):
        if char == english[slot]:
            final = final + rot13[slot]
print(final)
