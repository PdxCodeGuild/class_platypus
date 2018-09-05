# nums = [5, 0, 8, 3, 4, 1, 6]
#
# num = 0
# for num in nums:
#     print(num)
# total_nums = sum(nums)
# print(total_nums)
# average = total_nums / len(nums)
# print(average)




nums = []
while True:
    user_input = int(input(f"Enter a number, or 'done':"))
    if user_input!= 'done':
        nums.append(user_input)
    else:
        break
    total_nums = sum(nums)
    average = total_nums / len(nums)
    print(average)

# counts = list(word_dict())
# counts.sort(key=lambda tup: [1], reverse=true])
# print(counts)
