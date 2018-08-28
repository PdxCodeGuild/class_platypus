import re
# Opens and copies the text of a book's .txt file
with open('MobyDick.txt', 'r') as f:
    input_text = f.read()
f.close()
# Finds the number of characters (w/o spaces)
num_characters = len(input_text) - input_text.count(' ')
# Finds the number of words
num_words = len(re.compile('\w+').findall(input_text))
# Finds the number of sentences
end_sentence = '.!?'
num_sentences = 0
for i in range(len(input_text)):
    if input_text[i] in end_sentence:
        num_sentences += 1
# Calculates the Automated Readability Index (ARI)
ari = int(4.71 * (num_characters / num_words) + 0.5 * (num_words / num_sentences) - 21.43)
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
# Prints out appropriate ARI level for the imputed txt
print('The ARI for MobyDick.txt is ' + str(ari) + '.')
print('This corrsponds to a ' + ari_scale[ari]['grade_level'] + ' level of difficulty')
print('that is suitable for an average person ' + ari_scale[ari]['ages'] + ' years old.')