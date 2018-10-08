from statistics import mode

welcome_mess = print(f"\nWelcome to the Average, Median, and Mode Converter!\n")
final_data_set = []
data_set  = input('Please enter your data, separated by commas: ')
data_set = data_set.split(',')

for i in range(len(data_set)):
    i = data_set[i].strip(' ')
    final_data_set.append(i)


# average
def average():
    final_avg = [int(i) for i in final_data_set]
    final_avg = sum(final_avg)
    average = final_avg / len(final_data_set)
    print(f'The AVERAGE is: {average}')
    return

average()


#MEDIAN
def median():

    final_data_set.sort()
    if len(final_data_set) % 2 > 0:
        median_index = len(final_data_set) // 2
        median = final_data_set[median_index]
        print(f'The MEDIAN number is: {median}')

    else:
        median_index = len(final_data_set) // 2
        median = (final_data_set[median_index] + final_data_set[median_index - 1]) / 2
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

