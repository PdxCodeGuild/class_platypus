nums = [5, 0, 8, 3, 4, 1, 6]
sum=0
# loop over the indices
for i in range(len(nums)):
   sum = sum + nums[i]
average=sum/len(nums)
print(f"average of the list{nums} is {average}" )
