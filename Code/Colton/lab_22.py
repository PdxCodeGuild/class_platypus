
import string


#words in the text
def words_in_text():
    with open('wright_brothers.txt', 'r', encoding='utf-8') as f:
        contents = f.read()
    contents = contents.lower()
    punctuation = "/[-[\]{}()*+?.,\\^$|#\]/, \"\\$&"
    for char in punctuation:
        contents = contents.replace(char, ' ')
    contents = contents.split()
    count = 0
    for word in range(len(contents)):
        count += 1
    return float(count)


# characters in text
def char_in_text():
    with open('wright_brothers.txt', 'r', encoding='utf-8') as f:
        contents = f.read()
    contents = list(contents)
    num_char = 0
    for c in range(len(contents)):
        if contents[c] in string.ascii_letters:
            num_char += 1
    return float(num_char)




#sentences in a text
def sentences_in_text():
    with open('wright_brothers.txt', 'r', encoding='utf-8') as f:
        contents = f.read()
    contents = contents.lower()
    num_sentence = 0
    end_punc = '.?!'
    for c in range(len(contents)):
        if contents[c] in end_punc:
          num_sentence += 1
    return float(num_sentence)


ari = (4.71 * (char_in_text() / words_in_text()) + .05 * (words_in_text() / sentences_in_text()) - 21.43)



ari_scale ={
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
    14: {'ages': '18-22', 'grade_level':      'College'}}
ari = ari_scale[ari]
print(ari)