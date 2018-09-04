nums = []

#c = 0
while True:
    #for i in range(len(nums)):
     #   c += nums[i]

    #value = c//len(nums)
    #print(value)

    x = input('Enter a number, or "done": ').lower()
    if x == 'done':
        break
    else:
        nums.append(float(x))




#loop over the indices
c = 0
for i in range(len(nums)):
    c += nums[i]

value = c/len(nums)
print(value)



#loop over the indices



