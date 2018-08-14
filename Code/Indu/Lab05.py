# Random emoticon generator
import random
eyes = [':','D','o','$','%',':']
nose = ['|','i','^']
mouth = ['(',')','O','D']
out_string = ''
for i in [0,1,2,3]:
  out_string = out_string + random.choice(eyes)+random.choice(nose)+random.choice(mouth)
print(out_string)
