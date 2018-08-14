# Random emoticon generator
import random
eyes = [':','D','o','$','%',':']
nose = ['|','','o']
mouth = ['(',')','O','D']
out_string = ''
for i in [0,1,2,3,4,5,6]:
  out_string = out_string + random.choice(eyes)+random.choice(nose)+random.choice(mouth)
print(out_string)
