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
print (f"The sorted list is {sorted(nums)}")
length= len(nums)
print (length)
if length %2 != 0:
    print (f"The median of the list is {nums[(length-1)//2]}")
else:
    print(f"The median of list is {(nums[(length-1)//2]+ nums[(length+1)//2])/2}")


    #     return (l[(l_len - 1) / 2] + l[(l_len + 1) / 2]) / 2.0












