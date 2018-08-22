#lab 22 version 1
import math
import string

#to open a file
f = open('Nietzsche.txt', 'r')  # open the file
contents = (f.read()).lower() # read the contents and to lower

for p in string.punctuation:
    contents = contents.replace(p, ' ') #strips the punctuation

characters = contents.replace(' ', '')
print(characters)
#
# contents = contents.split() #puts all of the words into a list
#
# contents_length = len(contents) #how many words are in the list
#
# words = float(contents_length)
# sentences = float(input('how many sentences?  >   '))
# text = input('What book is this?  >   ')
#
# ari_equation = math.ceil(4.71 * (characters/words) + 0.5 *(words/sentences) - 21.43)
#
#
# ari_scale = {
#      1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
#      2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
#      3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
#      4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
#      5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
#      6: {'ages': '10-11', 'grade_level':    '5th Grade'},
#      7: {'ages': '11-12', 'grade_level':    '6th Grade'},
#      8: {'ages': '12-13', 'grade_level':    '7th Grade'},
#      9: {'ages': '13-14', 'grade_level':    '8th Grade'},
#     10: {'ages': '14-15', 'grade_level':    '9th Grade'},
#     11: {'ages': '15-16', 'grade_level':   '10th Grade'},
#     12: {'ages': '16-17', 'grade_level':   '11th Grade'},
#     13: {'ages': '17-18', 'grade_level':   '12th Grade'},
#     14: {'ages': '18-22', 'grade_level':      'College'}
# }
#
# print
# if ari_equation > 14:
#     print(f'The ARI for {text} is {ari_scale[1]}. ')
# else:
#      print('That is college level.')
# #
# #      This corresponds to a {ari_scale[11th Grade level of difficulty
# # that is suitable for an average person 16-17 years old.


f.close()  # close the file