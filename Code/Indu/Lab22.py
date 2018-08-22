import string

with open('grimm.txt', 'r', encoding='utf-8') as f:
    contents = f.read()  # read the contents
stop = [ '?','.']
word = ['?','.',';',':',' ']
num_sentence = 0
num_words = 0
num_character =0
i=0
for  i in range(len(contents)):
    if contents[i] in stop:
        num_sentence +=1
    else:
        num_sentence +=0
    if contents[i] in word:
        num_words +=1
    if contents[i] in string.ascii_letters:
        num_character +=1
print(num_sentence,num_words,num_character)
ari = 4.71*float(num_character/num_words)+0.5*float(num_words/num_sentence)-21.43
ari = round(ari + .5)
print(f"The ARI is {ari}")
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

ari = ari_scale[ari]
print(f"That text has an ARI for ages {ari['ages']} in {ari['grade_level']}")
# #
# # ari_scale = {'5-6': 'Kindergarten','6-7': '1st Grade','7-8':'2nd Grade','8-9':'3rd grade','9-10':'4th grade','10-11':'5thgrade',
# #      '11-12':'6th grade','12-13':'7th grade','13-14':'8th grade','14-15':'9th grade','15-16':'10th grade'}