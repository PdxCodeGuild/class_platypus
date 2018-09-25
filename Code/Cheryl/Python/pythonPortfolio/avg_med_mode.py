from statistics import mode

final_data_set = []
data_set  = input('Please enter your data: ')
data_set = data_set.split(',')

for i in range(len(data_set)):
    i = data_set[i].strip(' ')
    final_data_set.append(i)

# average
def average():
    nums = []
    running = 0

    try:
        # data_set = input('Please enter your number, or type \'done\' to get the average. >    ')
        # data_set = int(data_set)
        # data_set = round(data_set, 2)
        nums.append(data_set)
        print(nums)

    except ValueError:
        for num in nums:
            running += num
            running = round(running, 2)
        print('Adding your numbers now...')
        average = running / len(nums)
        print(f'The average is: {average}')

    return

average()


#MEDIAN
def median():
    nums = []
    running = 0
    median = ''


    try:
        # data_set = input('Please enter your number, or type \'done\' to get the median. >    ')
        # data_set = int(data_set)
        # data_set = round(data_set, 2)
        nums.append(data_set)
        print(nums)

    except ValueError:

        nums.sort()
        length = len(nums)

        if len(nums) % 2 > 0:
            median_index = len(nums) // 2
            median = nums[median_index]
            print(f'The median number is: {median}')

        else:
            median_index = len(nums) // 2
            median = (nums[median_index] + nums[median_index - 1]) / 2
            print(f'The median number is: {median}')

    return


median()

#mode


def data():
    try:

        # data_set = input('Please enter your data set. >  ')

        print(f"The MODE of this data set is: {mode(final_data_set)}")
        return
    except ValueError:
        print(f'There is no MODE in this data set: {data_set}')


data()

