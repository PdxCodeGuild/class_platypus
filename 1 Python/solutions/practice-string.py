
# Problem 1
#
# Get a string from the user, print out another string, doubling every letter.
#
# >>> Enter some text: hello
# hheelllloo

def double_your_fun(s):
    double = ''
    for i in range(len(s)):
        double = double + s[i] + s[i]
    return double

print(double_your_fun('platypus'))






# Problem 2
#
# Write a function that takes a string, and returns a list of strings, each missing a different character.
#
# missing_char('kitten') → ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']

def missing_fun(s):
    missing_char = []
    for i in range(len(s)):
        k = ''
        for j in range(len(s)):
            if j != i:
                k += s[j]
        missing_char.append(k)
    return missing_char

print(missing_fun('kitten'))


# Problem 3
#
# Return the letter that appears the latest in the english alphabet.
#
# >>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
# the latest letter is v.


# Problem 4
#
# Write a function that returns the number of occurances of 'hi' in a given string.
#
# count_hi('hihi') → 2


# Problem 5
#
# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'
#
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('catdogcatdog') → True


# Problem 6
#
# Return the number of letter occurances in a string.
#
# def count_letter(letter, word):
#     ...
# count_letter('i', 'antidisestablishmentterianism') → 5
# count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') → 2

def count_letter(letter, word):
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count += 1
    return count

print(count_letter('i', 'antidisestablishmentterianism'))
print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))


# Problem 7
#
# Convert input strings to lowercase without any surrounding whitespace.
#
# lower_case("SUPER!") → 'super!'
# lower_case("        NANNANANANA BATMAN        ") → 'nannananana batman'

