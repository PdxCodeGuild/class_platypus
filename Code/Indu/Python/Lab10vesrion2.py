nums = []
while True:
    num= input("Enter a number or enter done\n")
    if num != 'done':
        num=int(num)
        nums.append(num)

    else:
         break
print (nums)
sum=0
# loop over the indices
for i in range(len(nums)):
   sum = sum + nums[i]
average=sum/len(nums)
print(f"average of the list{nums} is {average}" )
