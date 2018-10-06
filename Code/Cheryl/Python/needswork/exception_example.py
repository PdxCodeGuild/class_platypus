import math


def split_check(total, number_of_people):
    cost_per_person = math.ceil(total / number_of_people)
    return cost_per_person


try:
    number_of_people = float(input('enter the number of people'))
    total_due = int(input('Enter the amount of the bill.'))
except ValueError:
    print("Oh no, that's not a number. Please enter a number.")
except ZeroDivisionError:
    print("You can't have zero people eating dinner. Please try again.")

else:
    amount_due = split_check(total_due, number_of_people)
    print(f"each person owes {amount_due}")