#Gets the users credit card number saved as a list
input_string = input('Enter in credit card number: ')
nums = list(input_string)
#Puts input string into list of ints
num_list = [int(num) for num in nums]
#Saves last digit as check_digit
check_digit = nums.pop(-1)
#Reverses list and removes check_digit
num_list = list(reversed(num_list[:len(num_list) - 1]))
for i in range(len(num_list)):
    #Doubles all values in even positions
    if i % 2 == 0:
        num_list[i] = num_list[i] + num_list[i]
    #Subtracts 9 from all values greater than 9
    if num_list[i] > 9:
        num_list[i] -= 9
#Gets the second digit of the sum of the list
second_digit = str(sum(num_list))[1]
#Checks if second_digit is valid for the check_digit
if second_digit == check_digit:
    print('Valid!')
else:
    print('Not valid.')