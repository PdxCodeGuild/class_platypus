import random
eye_list = (':', ';', ':')
nose_list = ('.', '>', '3' )
mouth_list = (')','(', 'p', 'D' )
i = 0
while i < 5:
    i = i + 1
    out_string = ''
    out_string = out_string + random.choice(eye_list) + random.choice(nose_list) + random.choice(mouth_list)
    print(out_string)